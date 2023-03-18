from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import user_passes_test
# Create your views here.
from .models import PersonData
from django.contrib.auth import authenticate, login


@user_passes_test(lambda u: u.is_superuser)
def admin_only_view(request):
    return render(request, 'admin_only.html')

def signup(request):
    template = loader.get_template('signup.html')
    context = {}
    return HttpResponse(template.render(context, request))

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        mydata = PersonData.objects.filter(username=username,password=password).values()
        if len(mydata) != 1:
            return HttpResponse("Login Failed")
        else:
            return redirect(f'dashboard', username=username)
    else:
        return render(request, 'login.html')


def homepage(request):
    template = loader.get_template('homepage.html')
    context = {}
    return HttpResponse(template.render(context, request))

def dashboard(request, username):
    template = loader.get_template('dashboard_client.html')
    mydata = PersonData.objects.filter(username=username).values()
    print(mydata[0])
    context = {"data":mydata[0]}
    return HttpResponse(template.render(context,request))

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
    context = {"n":"DATA INSERTED"}
    return HttpResponse(template.render(context, request))