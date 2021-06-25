from django.urls import path
from . import views

urlpatterns = [
    path("", views.display_index),
    path("index", views.display_index)
]