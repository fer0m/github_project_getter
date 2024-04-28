import django_filters
from .models import GitHubRepository


class GitHubRepositoryFilter(django_filters.FilterSet):
    min_stars = django_filters.NumberFilter(field_name="stargazers_count", lookup_expr='gte')
    max_stars = django_filters.NumberFilter(field_name="stargazers_count", lookup_expr='lte')
    language = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = GitHubRepository
        fields = ['stargazers_count', 'language']

