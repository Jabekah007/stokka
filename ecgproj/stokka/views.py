
from urllib import response
from django.contrib import messages
from django.shortcuts import redirect, render
#from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required




# Create your views here.
def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Credentials invalid')
            return redirect('signin')
    else:
        return render(request,"signin.html",{})

@login_required(login_url='signin')
def index(request):
    return render(request,"index.html")