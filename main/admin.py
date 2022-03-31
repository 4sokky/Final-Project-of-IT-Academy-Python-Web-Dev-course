from django.contrib import admin
from . import models


# admin.site.register(models.Articles)
admin.site.register(models.Comment)
admin.site.register(models.Profile)


@admin.register(models.Articles)
class ArticlesAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'article_subject', 'created_by', 'publish_at')
    list_filter = ('publish_at',)
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('article_subject', 'title')
