from django.shortcuts import render
from userApp.models import UserManage
from django.contrib.auth import logout
from django.shortcuts import redirect
# Create your views here.
from django.http import HttpResponse
def Home(req):
    return render(req,"home.html")

def reg(req):
    return render(req,'register.html')

def Register(request):
    print('entering')
    name = request.POST['Name']
    print(name,'name..')
    password = request.POST['Password']
    confirmpassword = request.POST['Confirmpassword']
    print('........entering')

    UserManage(username=name,password=password).save()
    return render(request, 'login.html')

def Login(reqest):
    return render(reqest,'login.html')

def loginView(request):
    print('entering into login view')
    name=request.POST.get('Name')
    print(name,'name////..')
    password=request.POST['Password']
    if name and password:        
        queryset = UserManage.objects.filter(username=name,password=password)
        
        return render(request,'bank.html')
    else:
        return HttpResponse('No valid user')
    
def Bank(request):
    return render(request,'bank.html')
def logout_view(request):
    logout(request)
    return redirect('home')
    