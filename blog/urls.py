from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from blog import views

urlpatterns = [
    path('', views.all_blogs, name='all_blogs'),

    ]
