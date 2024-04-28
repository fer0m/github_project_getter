from django.http import HttpResponseRedirect
from django.urls import reverse


class ErrorHandlingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        errors_to_redirect = [400, 404, 500]
        response = self.get_response(request)
        if response.status_code in errors_to_redirect:
            return HttpResponseRedirect(reverse('search_results'))
        return response
