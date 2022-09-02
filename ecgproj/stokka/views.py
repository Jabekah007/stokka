

from multiprocessing import context
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render

from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required
from .models import Inventory
from .forms import ProductForm








# Create your views here.

#READ
def data_read(request):
    context = {'dashboard':Inventory.objects.all()}
    return render(request,"dashboard.html",context)

#CREATE/
@login_required(login_url='signin')
def Inventory(request,id=None):
    if request.method == "POST":
        if id == None:
            form = ProductForm(request.POST)
        else:
            Inventory = Inventory.objects.get(pk=id)
            form = ProductForm(request.POST,instance = Inventory)
        if form.is_valid():
            form.save()   
        
    else:
        if id == None:
            form = ProductForm()
        else:
            Inventory = Inventory.objects.get(pk =id)
            form = ProductForm(instance=Inventory)
        return render(request,"inventory1.html",{'form':form})

#DELETE
@login_required(login_url='signin')
def data_delete(request,Inventory_id):
    Inventory = Inventory.objects.get(id = Inventory_id)
    Inventory.delete()
    return redirect('/dashboard')


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
    return render(request,"index.html",{})


@login_required(login_url='signin')
def base(request):
    return render(request,"base.html",{})
def dashboard(request):
    return render(request,"dashboard.html",{})








   