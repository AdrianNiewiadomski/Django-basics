from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


# A view function takes a request as an argument and returns HttpResponse.
def display_index(request):
    return HttpResponse("Hello, world!")
