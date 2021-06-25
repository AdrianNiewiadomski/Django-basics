from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest


# Now simply add arguments mentioned in urls.py as arguments of the view function.
def add_items(request, item1, item2):
    try:
        result = item1 + " + " + item2 + " = " + str(float(item1) + float(item2))
        # If the entered values are not numeric, the exception will be raised.

        return HttpResponse(result)
    except ValueError:
        # Instead of an ordinary HttpResponse, you may use an error response with the appropriate message.
        return HttpResponseBadRequest("An invalid number has been entered.")
