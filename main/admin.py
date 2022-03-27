from django.contrib import admin
from . import models


# Register your models here.
# admin.site.register(models.Articles)

@admin.register(models.Articles)
class ArticlesAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'article_subject', 'created_by', 'publish_at')
    list_filter = ('publish_at',)
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}      # TODO: What is it?
    ordering = ('article_subject', 'title')         # TODO: What is it?
