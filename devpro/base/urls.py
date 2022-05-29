from django.contrib import admin
from django.urls import path, include
from .views import index

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('index/', index, name='index')
]
