from django.urls import path
from . import views

urlpatterns = [
    # Postfix of the URL will be used to call a chosen view function.
    path("", views.display_index),
    # Multiple URLs may be routed to the same view function.
    path("index", views.display_index)
]
