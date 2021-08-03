
from django.urls import path
from django.views.generic.base import TemplateView
from django.contrib.auth import views as auth_views

from . import views
from .views import accounts

app_name = "accounts"
urlpatterns = [
    path("", accounts, name='accounts'),
    path('accounts/profile', views.ProfileView.as_view(), name = "profile"),
    #path('accounts/result', views.TemplateView.as_view(template_name="accounts/result.html")),

    # Django Auth
    path('accounts/login',
         auth_views.LoginView.as_view(template_name="accounts/login.html"), name='login'),
    path('accounts/logout',
         auth_views.LogoutView.as_view(), name='logout')
]