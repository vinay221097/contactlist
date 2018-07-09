from django.shortcuts import render
from django.http import *
from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from .models import Contacts
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

	
def login_user(request):
    logout(request)
    username = password = ''
    context={}
    if request.POST:
        username = request.POST['uname']
        password = request.POST['psw']

        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/index/')
    return render(request,"registration/login.html", context={'':request})

# @login_required(login_url='/login/')
def index(requests):
	contact_list=Contacts.objects.all()
	context={"contact":contact_list}
	return render(requests,"home.html",context)

def test(request):
	return render(request,"registration/login.html",context={})