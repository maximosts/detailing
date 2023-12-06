# search/urls.py
from django.urls import path
from . import views

app_name = 'search'  # This sets the app namespace

urlpatterns = [
    path('search/', views.search_items, name='search_items'),
]
