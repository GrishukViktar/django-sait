from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def communications(request):
    return render(request, 'main/communications.html')


def homework(request):
    return render(request, 'main/homework.html')



