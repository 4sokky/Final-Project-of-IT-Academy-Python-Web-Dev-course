from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


app_name = 'main'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:yy>_<int:mm>_<int:dd>/<slug:slug>', views.detailed_article, name="detailed_article"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
