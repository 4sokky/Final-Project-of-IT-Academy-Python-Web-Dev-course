from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponse
from . import models
from . import forms


# Create your views here.
def index(request):
    articles = models.Articles.objects.all()
    return render(request, 'main/index.html', {'articles': articles})


def detailed_article(request, yy, mm, dd, slug):
    article = get_object_or_404(models.Articles,
                                publish_at__year=yy,
                                publish_at__month=mm,
                                publish_at__day=dd,
                                slug=slug)
    return render(request, 'main/articles/detailed_article.html', {'article': article})


def admin_panel(request):
    articles = models.Articles.objects.all()
    return render(request, 'main/admin/admin_panel.html', {'articles': articles})


def create_article(request):
    if request.method == "POST":
        article_form = forms.ArticleForm(request.POST)
        if article_form.is_valid():
            new_article = article_form.save(commit=False)
            new_article.author = User.objects.first()       # TODO: Must be current user
            new_article.slug = new_article.title.replace(" ", "-")
            new_article.save()
            return render(request, "main/articles/detailed_article.html", {"article": new_article})
    else:
        article_form = forms.ArticleForm()
    return render(request, "main/admin/create_article.html", {"form": article_form})
