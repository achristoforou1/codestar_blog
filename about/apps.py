"""
App configuration for the about app.
Defines application-specific settings and metadata.
"""
from django.apps import AppConfig


class AboutConfig(AppConfig):
    """
    Configuration class for the :mod:`about` app.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'about'
