from django.urls import path
from .views import index, redirect_view

urlpatterns = [
    path('', index, name='index_url'),
    path('short/<str:code>/', redirect_view, name='redirect_url'),
]