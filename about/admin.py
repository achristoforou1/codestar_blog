"""
Django admin configuration for the about app.
Registers the About and CollaborateRequest models with admin interface customizations.
"""
from django.contrib import admin
from .models import About, CollaborateRequest
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    """
    Admin interface options for the :model:`about.About` model.
    Enables Summernote editing for the `content` field.
    """
    summernote_fields = ('content',)

# Register CollaborateRequest normally
@admin.register(CollaborateRequest)
class CollaborateRequestAdmin(admin.ModelAdmin):
    """
    Admin interface options for the :model:`about.CollaborateRequest` model.
    Includes list display, filters, and search options.
    """
    list_display = ('name', 'email', 'read')
    list_filter = ('read',)
    search_fields = ('name', 'email', 'message')
