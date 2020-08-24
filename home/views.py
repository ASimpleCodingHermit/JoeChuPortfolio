from django.shortcuts import render, HttpResponse

# Create your views here.


def home(request):
    context = {"name": "Joe", "jobTitle": "Full Stack Developer"}
    return render(request, 'home.html', context)


def about(request):
    return render(request, 'about.html')


def projects(request):
    return render(request, 'projects.html')


def blog(request):
    return render(request, 'blog.html')


def contact(request):
    return render(request, 'contact.html')
