from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from django.contrib.auth.models import User
from . import models
from . import forms


def index(request):
    articles = models.Articles.objects.all()
    return render(request, 'main/index.html', {'articles': articles})


def detailed_article(request, yy, mm, dd, slug):
    article = get_object_or_404(models.Articles,
                                publish_at__year=yy,
                                publish_at__month=mm,
                                publish_at__day=dd,
                                slug=slug)
    if request.method == 'POST':
        comments_form = forms.CommentsForm(request.POST)
        if comments_form.is_valid():
            new_comment = comments_form.save(commit=False)
            new_comment.article = article
            new_comment.save()
            return redirect(article)
    else:
        comments_form = forms.CommentsForm()
    return render(request, 'main/articles/detailed_article.html', {'article': article,
                                                                   'form': comments_form})


@login_required
def admin_panel(request):
    articles = models.Articles.objects.all()
    return render(request, 'main/admin/admin_panel.html', {'articles': articles})


@login_required
def create_article(request):
    if request.method == 'POST':
        article_form = forms.ArticleCreateForm(request.POST)
        if article_form.is_valid():
            new_article = article_form.save(commit=False)
            new_article.author = User.objects.first()       # TODO: Must be current user
            new_article.slug = new_article.title.replace(" ", "-")
            new_article.save()
            return redirect(new_article)
    else:
        article_form = forms.ArticleCreateForm()
    return render(request, "main/admin/create_article.html", {"form": article_form})


@login_required
def edit_article(request, slug):
    article = models.Articles.objects.get(slug=slug)
    form = forms.ArticleEditForm(instance=article)
    if request.method == 'POST':
        form = forms.ArticleEditForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect(article)
    return render(request, 'main/admin/edit_article.html', {'form': form})


@login_required
def delete_article(request, slug):
    article = models.Articles.objects.get(slug=slug)
    if request.method == 'POST':
        article.delete()
        return redirect('/admin_panel/')
    return render(request, 'main/admin/delete_article.html', {'article': article})


# @login_required
def profile_view(request):
    return render(request, 'main/profile.html')


def register(request):
    if request.method == "POST":
        user_form = forms.RegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data["password"])
            new_user.save()
            models.Profile.objects.create(user=new_user, avatar="nophoto.jpg")
            return render(request, 'registration/registration_complete.html', {'new_user': new_user})
        else:
            return HttpResponse('Something went wrong..')
    else:
        user_form = forms.RegistrationForm(request.POST)
        return render(request, 'registration/register_user.html', {'form': user_form})
