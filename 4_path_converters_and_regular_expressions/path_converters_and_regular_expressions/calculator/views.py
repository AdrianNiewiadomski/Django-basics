from django.shortcuts import render

# Create your views here.


def display_calculator(request):
    return render(request, 'calculator/calculator.html')
