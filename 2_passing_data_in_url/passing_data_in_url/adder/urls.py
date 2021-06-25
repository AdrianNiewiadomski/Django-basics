from django.urls import path
from . import views

urlpatterns = [
    # To pass arguments from an URL to function use angle brackets.
    path("<item1>/<item2>", views.add_items)
]