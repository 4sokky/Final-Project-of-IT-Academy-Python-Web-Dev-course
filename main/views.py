from django.shortcuts import render
from django.http import HttpResponse
from . import models


# Create your views here.
def index(request):
    articles = models.Articles.objects.all()
    return render(request, 'main/index.html', {'articles': articles})
