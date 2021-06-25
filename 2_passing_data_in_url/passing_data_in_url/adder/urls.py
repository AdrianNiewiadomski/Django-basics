from django.urls import path
from . import views

urlpatterns = [
    path("<item1>/<item2>", views.add_items)
]