from django.shortcuts import render, HttpResponse

# Create your views here.


def home(request):
    return HttpResponse('this is my home page (/)')


def about(request):
    return HttpResponse('this is my about page (/about)')


def projects(request):
    return HttpResponse('this is my projects page (/projects)')


def blog(request):
    return HttpResponse('this is my blog page (/blog)')


def contact(request):
    return HttpResponse('this is my contact page (/contact)')
