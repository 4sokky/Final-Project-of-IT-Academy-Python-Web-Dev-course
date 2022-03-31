from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.urls import reverse_lazy
from django.conf.urls.static import static
from . import views


app_name = 'main'


class PWResetDoneHack(auth_views.PasswordResetView):
    success_url = reverse_lazy('main:password_reset_done')


urlpatterns = [
    path('', views.index, name='index'),
    path('<int:yy>_<int:mm>_<int:dd>/<slug:slug>/', views.detailed_article, name="detailed_article"),

    path('admin_panel/', views.admin_panel, name='admin_panel'),
    path('admin_panel/create_article/', views.create_article, name='create_form'),
    path('admin_panel/edit_article/<str:slug>/', views.edit_article, name='edit_article'),
    path('admin_panel/delete_article/<str:slug>/', views.delete_article, name='delete_article'),

    path('registration/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('password_reset/', PWResetDoneHack.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        success_url=reverse_lazy('main:password_reset_complete')), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    path('profile/', views.profile_view, name='profile'),   # TODO: Must be url with slug or id
    path('profile/edit/', views.edit_profile, name='edit_profile')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
