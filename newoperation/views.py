from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render,redirect
from django.views.generic import View,TemplateView,FormView,ListView,DetailView,UpdateView
from newoperation.forms import RegistrationForm,LoginForm,OlxnewCreateForm,OlxNewChangeForm
from newoperation.models import OlxNew
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator

# Create your views here.

def signin_required(fn):
    def wrapper(request,*args,**kwargs):
        if not request.user.is_authenticated:
            messages.error(request,"invalid session...pls login..")
            return redirect("signin-olx")
        else:
            return fn(request,*args,**kwargs)
        
    return wrapper

class SignUpView(View):
    def get(self,request,*args,**kwargs):
       form=RegistrationForm()
       return render(request,"olx_reg.html",{"form":form}) 


    def post(self,request,*args,**kwargs):
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"registration successfully")
            return redirect("signin-olx")
        else:
            messages.error(request,"failed.......")
            return render(request,"olx_reg.html",{"form":form})
        

class SigninView(View):
    def get(self,request,*args,**kwargs):
        form=LoginForm()
        return render(request,"olx_login.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            usr=authenticate(request,username=uname,password=pwd)
            if usr:
                login(request,usr)
                messages.success(request,"successfully login..")
                return redirect("add-olx")
            else:
                messages.error(request,"failed.......")
            return render(request,"olx_login.html",{"form":form})
        
@method_decorator(signin_required,name="dispatch")
class IndexView(TemplateView):
    template_name ="index.html"

@method_decorator(signin_required,name="dispatch")  
class OlxCreateView(FormView):
    template_name ="newoperation/olx_add.html"
    form_class =OlxnewCreateForm

    def post(self,request,*args,**kwargs):
        form=OlxnewCreateForm(request.POST,files=request.FILES)
        if form.is_valid():
            OlxNew.objects.create(**form.cleaned_data,user=request.user)
            messages.success(request,"successfull...")
            return redirect("list-olx")
        else:
            messages.error(request,"failed...")
            return render(request,"newoperation/olx_add.html")
        
@method_decorator(signin_required,name="dispatch")
class OlxNewListView(ListView):
    template_name = "newoperation/olx_list.html"
    context_object_name ="vehicles"
    model=OlxNew

    def get_queryset(self):
        qs=OlxNew.objects.filter(user=self.request.user)
        return qs

@method_decorator(signin_required,name="dispatch")
class OlxNewDetailView(DetailView):
    template_name ="newoperation/olx_view.html"
    context_object_name ="vehicle"
    model=OlxNew

@method_decorator(signin_required,name="dispatch")
class OlxNewUpdateView(UpdateView):
    template_name = "newoperation/olx_update.html"
    model=OlxNew
    form_class = OlxNewChangeForm
    success_url =reverse_lazy("list-olx")

@signin_required
def remove_vehicle(request,*args,**kwargs):
    id=kwargs.get("pk")
    OlxNew.objects.filter(id=id).delete()
    return redirect("list-olx")

def signout(request,*args,**kwargs):
    logout(request)
    return redirect("signin-olx")