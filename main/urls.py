from django.urls import path
from . import views
app_name = 'search'

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search_items, name='search_items'),
    path('delete_comment/<int:comment_id>/', views.delete_comment, name='delete_comment'),
    # Add more URL patterns for additional views if needed
]
