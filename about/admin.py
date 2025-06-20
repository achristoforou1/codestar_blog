from django.contrib import admin
from .models import About, CollaborateRequest
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)

# Register CollaborateRequest normally
@admin.register(CollaborateRequest)
class CollaborateRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'read')
    list_filter = ('read',)
    search_fields = ('name', 'email', 'message')
