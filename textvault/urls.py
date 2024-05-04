"""
URL configuration for textvault project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path,include 
from django.contrib import admin

from textapp.views import *

# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )

urlpatterns = [
    path("admin/", admin.site.urls),
  
    path('login/', login_user, name='login'),
    path('refresh/',refresh_token, name='refresh'),
    path('create_snippet/',create_snippet, name='create_snippet'),
    path('snippet_detail/<int:snippet_id>/', snippet_detail, name='snippet_detail'),
    path('get_all_snippets/', get_all_snippets, name='get_all_snippets'),
    path('update_snippet/<int:snippet_id>/', update_snippet, name='update_snippet'),
    path('delete_snippets/', delete_snippets, name='delete_snippets'),
    path('get_all_tags/', get_all_tags, name='get_all_tags'),
    path('snippets_by_tag_id/<int:tag_id>/', snippets_by_tag_id, name='snippets_by_tag_id'),

 
]



