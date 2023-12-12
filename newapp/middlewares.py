from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponse
from django.http import Http404
from django.http import JsonResponse
from rest_framework import status

from django.utils.deprecation import MiddlewareMixin
from django.http import JsonResponse, Http404

from django.http import HttpResponse, Http404

class Custom404ExceptionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self,  request, *args, **kwargs):
        print("Before Middleware Called")
        response = self.get_response(request)
        # if exception:
        #     message = "Sorry, the page was not found."
        #     return JsonResponse(message, status=404)
        #
        # message = "An unexpected error occurred."
        # return JsonResponse(message, status=500)

        if response.status_code == 404:
            return JsonResponse({"error":"Sorry, the page was not found."}, status=status.HTTP_404_NOT_FOUND)
        return response

    def process_exception(self, request, exception):
        if exception:
            message = "Sorry, the page was not found."
            return JsonResponse(message, status=404)

        message = "An unexpected error occurred."
        return JsonResponse(message, status=500)


class MyTemplateMiddleware:
    def __init__(self, response):
        self.response = response
        print("MyTemplateMiddleware")

    def __call__(self, request, *args, **kwargs):
        print("Before Middleware Called")
        response = self.response(request)
        print("After:  Middleware Called")

        return response
    def process_template_response(self, request, response):
        print("Process Template Response")
        response.context_data['a'] = 6
        return response
