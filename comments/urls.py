# comments/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('post_comment/', views.post_comment, name='post_comment'),
    path('delete_comment/<int:comment_id>/', views.delete_comment, name='delete_comment'),
]
