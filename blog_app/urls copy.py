"""BLOG URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from blog_app import views
from django.urls import path

urlpatterns = [
    path('', views.post_list, name='post-list'),
    path("post-detail/<int:pk>/", views.post_detail, name="post-detail"),
    path('draft-list/', views.draft_list, name='draft-list'),
    path('post-create/', views.post_create, name='post-create'),
    path("post-publish/<int:pk>/", views.post_publish, name="post-publish"),
    path("post-delete/<int:pk>/", views.post_delete, name="post-delete"),
    path("post-update/<int:pk>/", views.post_update, name="post-update"),

]
