from typing import Any
from django.shortcuts import render,redirect
from django.views.generic import View
from operation.forms import olxCreateForm,OlxChangeForm,RegistrationForm,LoginForm
from operation.models import Olx
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def signout(request,*args,**kwargs):
    logout(request)
    return redirect("signin")


class SignUpView(View):
    def get(self,request,*args,**kwargs):
        form=RegistrationForm()
        return render(request,"registration.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=RegistrationForm(request.POST)
        if form.is_valid():
            User.objects.create_user(**form.cleaned_data)
            return redirect("signin")
        else:
            return render(request,"registration.html",{"form":form})


class SigninView(View):
    def get(self,request,*args,**kwargs):
        form=LoginForm()
        return render(request,"login.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pswrd=form.cleaned_data.get("password")
            usr=authenticate(request,username=uname,password=pswrd)
            if usr:
                login(request,usr)
                print("credential valid...")
                return redirect("olx-add")
            else:
                print("credential invalid....")
                return render(request,"login.html",{"form":form})

class olxCreateView(View):
    def get(self,request,*args,**kwargs):
        form = olxCreateForm()
        return render(request,"olx_add.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=olxCreateForm(request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            print("add new one.....")
            return render(request,"olx_add.html",{"form":form})
        else:
            return render(request,"olx_add.html",{"form":form})
        
class OlxListView(View):
    def get(self,request,*args,**kwargs):
        qs=Olx.objects.all()
        return render(request,"olx_list.html",{"vehicles":qs})
    
class OlxDetailView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Olx.objects.get(id=id)
        return render(request,"olx_detail.html",{"vehicle":qs})
    
class OlxDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Olx.objects.get(id=id).delete()
        return redirect("olx-list")
    
class OlxUpadateView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        obj=Olx.objects.get(id=id)

        form=OlxChangeForm(instance=obj)
        return render(request,"olx_edit.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        obj=Olx.objects.get(id=id)
        form=OlxChangeForm(request.POST,instance=obj,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect("olx-list")
        else:
            return render(request,"olx_edit.html",{"form":form})