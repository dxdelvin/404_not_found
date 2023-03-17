from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.
from .models import PersonData



def signup(request):
    template = loader.get_template('signup.html')
    context = {}
    return HttpResponse(template.render(context, request))

def login(request):
    template = loader.get_template('login.html')
    context = {}
    return HttpResponse(template.render(request, context))


def homepage(request):
    template = loader.get_template('homepage.html')


    context = {}
    return HttpResponse(template.render(request, context))

def saveform(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        birth_date = request.POST.get('birth_date')
        height = request.POST.get('height')
        weight = request.POST.get('weight')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        phone_number = request.POST.get('phone_number')
        email_id = request.POST.get('email_id')
        add_image = request.FILES.get('add_image')

        cont = PersonData(first_name=first_name,last_name = last_name,
                          username=username,birth_date=birth_date,height=height,
                          weight=weight,address=address,gender=gender,
                          phone_number=phone_number,email_id=email_id,
                          add_image=add_image)
        cont.save()

    template = loader.get_template('upload_success.html')
    conte = {}
    return HttpResponse(template.render(request, context=conte))