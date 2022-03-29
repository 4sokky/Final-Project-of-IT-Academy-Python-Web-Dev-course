from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


app_name = 'main'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:yy>_<int:mm>_<int:dd>/<slug:slug>', views.detailed_article, name="detailed_article"),
    path('admin_panel/', views.admin_panel, name='admin_panel'),
    path('admin_panel/create_article/', views.create_article, name='create_form'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
