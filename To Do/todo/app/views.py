from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout
from django.contrib import messages
from app.forms import *
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='login')
def Logout(request):
    logout(request)
    return redirect('login')
def add_todo(request):
    if request.user.is_authenticated:
        user=request.user
        print(user)
        form=TODOForm(request.POST)
        if form.is_valid():
           print(form.cleaned_data)
           todo=form.save(commit=False)
           todo.user=user
           todo.save()
           print(todo)
           return redirect("homepage")
        else:
           return render(request,'index.html',context={'form':form})
             
    
def home(request):
    if request.user.is_authenticated:
        user=request.user
        form=TODOForm()
        todos=TODO.objects.filter(user=user)
        return render(request,'index.html',context={'form':form,'todos':todos})

def Login(request):
    if request.method == "POST":
    



        username = request.POST.get('username')

        password = request.POST.get('password')




        validate_user = authenticate(username=username, password=password)




        if validate_user is not None:

            auth_login(request, validate_user)

            return redirect('homepage')

        else:

            messages.error(

                request, 'Error, wrong credentials or user not exists')

            return redirect('login')




    return render(request, "login.html")
    #  if request.method=='POST':
    #         username=request.POST.get('username')
    #         password=request.POST.get('password')
    #         user=authenticate(username=username,password=password)
    #         if user is not None:
    #             auth_login(request,user)
    #             print(user)
    #             return redirect('homepage')
    #         else:
    #             messages.error(request, 'The given Username or password is not valid!!!')
    #  return render(request,'login.html')

def Signup(request):
     if request.method=='POST':
          
         
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        user= User.objects.filter(username=username)
        
        
        if user.exists():
            messages.error(request,'Username already exist')
            return render(request,'signup.html')
        k,j,d=0,0,0
        if len(email)>=6:
            if email[0].isalpha():
                if ("@" in email) and (email.count("@")==1):
                    if (email[-4]==".") ^ (email[-3]=="."):
                        for i in email:
                          if i==i.isspace():
                            k=1
                          elif i.isalpha():
                            if i==i.upper():
                              j=1
                          elif i.isdigit():
                             continue
                          elif i=="_" or i=="." or i=="@":
                             continue
                          else:
                             d=1
                        if k==1 or j==1 or d==1:
                           messages.error(request,'Email is not valid')
                    else:
                        messages.error(request,'Email is not valid')
                else:
                    messages.error(request,'Email is not valid')
            
            else:
                messages.error(request,'Email is not valid')
        
        else:
            messages.error(request,'Email is not valid')
        
        
        
        user=User.objects.create_user(username=username,email=email,password=password)
        user.save()
     return render(request,'signup.html')