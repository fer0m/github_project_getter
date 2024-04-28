# Generated by Django 5.0.4 on 2024-04-26 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GitHubRepository',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('html_url', models.URLField()),
                ('stargazers_count', models.IntegerField()),
                ('avatar_url', models.URLField()),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField()),
            ],
        ),
    ]