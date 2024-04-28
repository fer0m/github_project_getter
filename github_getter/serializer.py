from rest_framework import serializers

from github_getter.models import GitHubRepository


class GitHubRepositorySerializer(serializers.ModelSerializer):
    class Meta:
        model = GitHubRepository
        fields = ['id', 'name', 'description', 'stargazers_count', 'language']
