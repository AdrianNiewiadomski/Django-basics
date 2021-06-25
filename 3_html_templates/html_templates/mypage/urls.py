from django.urls import path
from . import views

urlpatterns = [
    path('', views.display_index),
    path('about', views.display_about),
    path('contact', views.display_contact),
]
