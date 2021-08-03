from django.urls import path
#from django.views.generic.base import TemplateView

from . import views

app_name = "public"
urlpatterns = [

    path('', views.index, name="index"),
    path('about/', views.about, name="about"),

]