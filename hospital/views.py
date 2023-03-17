from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.


def homepage(request):
    template = loader.get_template('homepage.html')
    context = {}
    return HttpResponse(template.render(context, request))

def signup(request):
    template = loader.get_template('signup.html')
    context = {}
    return HttpResponse(template.render(context, request))

def login(request):
    template = loader.get_template('login.html')
    context = {}
    return HttpResponse(template.render(context, request))

def homepage(request):
    template = loader.get_template('homepage.html')
    context = {}
    return HttpResponse(template.render(context, request))

def data_recieve(request):
    pass