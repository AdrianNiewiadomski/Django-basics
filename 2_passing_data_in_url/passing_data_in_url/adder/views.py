from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def add_items(request, item1, item2):
    result = item1 + " + " + item2 + " = " + str(int(item1) + int(item2))
    return HttpResponse(result)
