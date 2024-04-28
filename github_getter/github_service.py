import json
from urllib.parse import urlencode

import requests


class GitHubService:
    BASE_URL = 'https://api.github.com/search/repositories'

    @staticmethod
    def search_repositories(language, per_page, start_date):
        query_parts = []
        if language:
            query_parts.append(f"language:{language}")
        if start_date:
            query_parts.append(f"created:{start_date}")

        query = ' '.join(query_parts)
        query_params = {
            'q': query,
            'sort': 'stars',
            'order': 'desc',
            'per_page': per_page
        }

        query_string = urlencode(query_params, safe='+')
        full_url = f"{GitHubService.BASE_URL}?{query_string}"
        response = requests.get(full_url)
        if response.status_code == 200:
            return json.loads(response.content)
        return None
