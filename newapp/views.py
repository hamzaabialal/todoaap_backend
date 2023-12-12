from django.shortcuts import render
from .models import ToDoModel
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
# Create your views here.
from .serializers import ToDoSerializer
from django.views.generic import TemplateView
from django.http import Http404


class ToDOListAPIView(ListCreateAPIView):
    queryset = ToDoModel.objects.all()
    serializer_class = ToDoSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ToDoDetailUpdateAPIView(RetrieveUpdateDestroyAPIView):
    queryset = ToDoModel.objects.all()
    serializer_class = ToDoSerializer

    def get(self, request, *args, **kwargs):

        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class Test(TemplateView):
    template_name = 'test.html'

    def get_context_data(self, *args, **kwargs):
        a = 6   # This line raises a ZeroDivisionError
        b = 7
        c = b / a
        # The code below won't execute because the function has already returned
        # Raise an Http404 here
        raise Http404("This is a 404 error message")


class FilterCompleteToDoList(ListCreateAPIView):
    queryset = ToDoModel.objects.filter(completed=True)
    serializer_class = ToDoSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class FilterIncompleteToDoList(ListCreateAPIView):
    queryset = ToDoModel.objects.filter(completed=False)
    serializer_class = ToDoSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class FilterToDoLIst(ListCreateAPIView):
    queryset = ToDoModel.objects.filter(title__icontains='a')
    serializer_class = ToDoSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class FilterToDoByName(ListCreateAPIView):
    queryset = ToDoModel.objects.filter(title__icontains='hamza')
    serializer_class = ToDoSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class FilterToDoByPriority(ListCreateAPIView):
    queryset = ToDoModel.objects.filter(title__icontains='important')
    serializer_class = ToDoSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)




