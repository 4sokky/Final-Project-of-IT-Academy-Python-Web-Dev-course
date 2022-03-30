from django import forms
from . import models


class ArticleCreateForm(forms.ModelForm):
    class Meta:
        model = models.Articles
        fields = ('title', 'body', 'article_subject', 'image', 'created_by')
        # TODO: Don't need to choose user
        # TODO: Fix img upload from form
        # TODO: Limit characters for fields


class ArticleEditForm(forms.ModelForm):
    class Meta:
        model = models.Articles
        fields = ('title', 'body', 'article_subject', 'image', 'created_by')


class CommentsForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ('name', 'body')
