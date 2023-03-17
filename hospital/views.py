from django.shortcuts import render
from django.shortcuts import HttpResponse, render

# Create your views here.


def homepage(request):
    render(request, "./hospital/templates/login.html")