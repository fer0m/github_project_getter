from datetime import datetime
from datetime import timezone as tz
from django.shortcuts import render, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView

from github_getter.filters import GitHubRepositoryFilter
from github_getter.github_service import GitHubService
from github_getter.models import GitHubRepository
from github_getter.serializer import GitHubRepositorySerializer

BASE_URL = 'https://api.github.com/search/repositories'


def search_results(request):
    context = {}
    if request.method == 'GET' and 'search' in request.GET:
        language = request.GET.get('language', '')
        per_page = request.GET.get('per_page', '10')
        start_date_str = request.GET.get('start_date', '')

        response_json = GitHubService.search_repositories(language, per_page, start_date_str)
        if response_json:
            context = prepare_models_from_response(response_json)
            if response_json.get("total_count") == 0:
                context = {"info": "No result was found for this query. Please check the query parameters."}
        else:
            context = {"info": "There was a problem fetching the data. Please try again."}
    return render(request, 'github_getter/search_template.html', context)


def prepare_models_from_response(response_json):
    repositories = []
    if not response_json.get('items'):
        return {}
    for repo_data in response_json.get('items'):
        naive_datetime = datetime.strptime(repo_data.get('created_at'), '%Y-%m-%dT%H:%M:%SZ')
        aware_datetime = timezone.make_aware(naive_datetime, tz.utc)

        repo, created = GitHubRepository.objects.update_or_create(
            name=repo_data.get('name'),
            defaults={
                'html_url': repo_data.get('html_url'),
                'stargazers_count': repo_data.get('stargazers_count'),
                'avatar_url': repo_data.get('owner', {}).get('avatar_url', ''),
                'description': repo_data.get('description') if repo_data.get('description') else "",
                'created_at': aware_datetime,
                'language': repo_data.get("language", ''),
            }
        )
        repositories.append(repo)

    return {'repositories': repositories}


def list_repositories(request):
    repositories_list = GitHubRepository.objects.all().order_by('-stargazers_count')
    paginator = Paginator(repositories_list, 10)
    page_number = request.GET.get('page')
    repositories = paginator.get_page(page_number)
    return render(
        request,
        'github_getter/list_repositories.html',
        {'repositories': repositories})


class GitHubRepositoryList(ListAPIView):
    queryset = GitHubRepository.objects.all()
    serializer_class = GitHubRepositorySerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = GitHubRepositoryFilter
