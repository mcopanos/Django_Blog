from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    template = 'blog/home.html'
    context = {
        'greeting': 'Welcome Home'
    }
    return render(request, template, context)


def about(request):
    template = 'blog/about.html'
    return render(request, template)


def blog(request):
    template = 'blog/list.html'
    return render(request, template)


def details(request):
    template = 'blog/details.html'
    return render(request, template)
