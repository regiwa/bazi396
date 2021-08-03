from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
#from django.template import loader

from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


def index(request: HttpRequest) -> HttpResponse:
    return render(request, "index.html")
    #template = loader.get_template('index.html')
    #return HttpResponse(template.render({}, request))

def about(request: HttpRequest) -> HttpResponse:
    return render(request, "about.html")

def contact(request: HttpRequest) -> HttpResponse:
    return render(request, "contact.html")

class ProfileView(LoginRequiredMixin,TemplateView):
    template_name = "accounts/profile.html"