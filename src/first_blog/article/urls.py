"""first_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework import routers

from .api import PostViewSet
router = routers.DefaultRouter()
router.register('api/article', PostViewSet, basename='article')
urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    # path('$/', Post, name='posts'),
    # path('$/', views.comments, name='comments'),
    path('home/', views.index, name='index'),
    path('post/<int:post_id>', views.post_detail, name='post_detail'),
    path('post/create', views.create_post, name='create_post'),
    path('post/createmf', views.create_post_mf, name='create_post_mf'),
    path('posts/', views.post_list, name='post_list'),
    path('new/', views.something_new, name='something_new')

]
# urlpatterns = router.urls
