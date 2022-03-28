from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . import models


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
