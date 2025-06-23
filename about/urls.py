"""
URL configuration for the about app.

Defines the URL pattern for the about page which is handled by the
`about_me` view.
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.about_me, name='about'),
]

