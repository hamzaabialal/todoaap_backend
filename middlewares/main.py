from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponse
from django.http import Http404


from django.utils.deprecation import MiddlewareMixin
from django.http import JsonResponse, Http404

class Custom404ExceptionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request, *args, **kwargs):
        print("Before Middleware Called")
        response = self.get_response(request)
        print("After:  Middleware Called")

        return response

    def process_exception(self, request, exception):
        if isinstance(exception, Http404):
            message = "Sorry, the page was not found."
            return HttpResponse(message, status=404)

        message = "An unexpected error occurred."
        return HttpResponse(message, status=500)
