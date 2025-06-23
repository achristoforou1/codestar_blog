"""
Configuration for the blog app.
Defines the default app configuration class.
"""
from django.apps import AppConfig


class BlogConfig(AppConfig):
    """
    Configuration class for the blog application.
    Sets the default name for the app as 'blog'.
    """

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
