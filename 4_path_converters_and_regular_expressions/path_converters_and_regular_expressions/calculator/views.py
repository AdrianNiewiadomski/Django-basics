from django.shortcuts import render
from .calculator import Calculator

operations = {
    'add': ['+', Calculator.add],
    'sub': ['-', Calculator.subtract],
    'mul': ['*', Calculator.multiply],
    'div': ['/', Calculator.divide]
}


def display_calculator(request):
    args = None
    if request.GET.get('x'):
        args = {
            'x': request.GET.get('x'),
            'op_name': request.GET.get('op'),
            'y': request.GET.get('y'),
            'op': operations[request.GET.get('op')][0],
            'result': operations[request.GET.get('op')][1](request.GET.get('x'), request.GET.get('y'))
        }
    return render(request, 'calculator/calculator.html', args)
