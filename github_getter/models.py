from django.db import models
# Create your models here.


class GitHubRepository(models.Model):
    name = models.CharField(max_length=255)
    html_url = models.URLField()
    stargazers_count = models.IntegerField()
    avatar_url = models.URLField()
    description = models.TextField(null=True, blank=True, default="")
    language = models.TextField(null=True, blank=True, default="")
    created_at = models.DateTimeField()

    def __str__(self):
        return self.name
