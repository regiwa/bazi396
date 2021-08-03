from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
#from django.template import loader




def index(request: HttpRequest) -> HttpResponse:
    return render(request, "index.html")
    #template = loader.get_template('index.html')
    #return HttpResponse(template.render({}, request))

def about(request: HttpRequest) -> HttpResponse:
    return render(request, "about.html")



