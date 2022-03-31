from django import forms
from . import models
from django.contrib.auth.models import User


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


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password:', widget=forms.PasswordInput)
    password_repeat = forms.CharField(label='Repeat password:', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password_repeat(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password_repeat']:
            raise forms.ValidationError('Passwords are different!')
        return cd['password_repeat']


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = models.Profile
        fields = ('birthday', 'avatar')
