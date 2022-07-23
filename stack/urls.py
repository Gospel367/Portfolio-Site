from venv import create
from django.urls import path
from .  import views

urlpatterns = [
    path('home',  views.PostList.as_view(), name='home1'),
    path('create/', views.CreatePost.as_view(), name='creator')
]
