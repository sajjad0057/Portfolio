from django.contrib import admin

from django_summernote.admin import SummernoteModelAdmin
from .models import Blog,Comment

# Register your models here.

# Apply summernote to all TextField in model.
class BlogAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = ('details',)
    list_display = ('user', 'title', 'image', 'slug','created_at','updated_at')
    fields = ('user','title','details','image')
    list_filter = ("title",)
    search_fields = ['title',]
    


class CommentAdmin(admin.ModelAdmin):
    list_display = ['blog','name','comment','created_at']

admin.site.register(Blog,BlogAdmin)
admin.site.register(Comment,CommentAdmin)
