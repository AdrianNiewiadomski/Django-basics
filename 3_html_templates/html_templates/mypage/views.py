from django.shortcuts import render
from django.http import HttpResponse


def display_index(request):
    # To display an HTML template instead of a string, use a template method.
    return render(request, 'mypage/template.html')


def display_about(request):
    return HttpResponse("about")


def display_contact(response):
    return HttpResponse('contact')
