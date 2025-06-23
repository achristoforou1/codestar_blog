"""
Django admin configuration for the blog app.
Registers the Post and Comment models with custom admin options.
"""
from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """
    Admin interface options for the :model:`blog.Post` model.
    Includes list display, search, filters, and Summernote integration. 
    """
 
   
     
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


# Register your models here.
admin.site.register(Comment) 
