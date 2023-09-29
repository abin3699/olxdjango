from django import forms
from operation.models import Olx
from django.contrib.auth.models import User



class RegistrationForm(forms.ModelForm):
    class Meta:
        model=User
        fields=["username","email","password"]
        widgets={
            "username":forms.TextInput(attrs={"class":"form-control"}),
            "email":forms.EmailInput(attrs={"class":"form-control"}),
            "password":forms.PasswordInput(attrs={"class":"form-control"})
        }

class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))

class olxCreateForm(forms.ModelForm):
    class Meta:
        model = Olx
        fields ="__all__"
        widget ={
            "name":forms.TextInput(attrs={"class":"form-control"}),
            "brand":forms.TextInput(attrs={"class":"form-control"}),
            "modelyr":forms.TextInput(attrs={"class":"form-control"}),
            "types":forms.TextInput(attrs={"class":"form-control"}),
            "owner":forms.TextInput(attrs={"class":"form-control"}),
            "km":forms.TextInput(attrs={"class":"form-control"}),
            "price":forms.TextInput(attrs={"class":"form-control"}),
        }

class OlxChangeForm(forms.ModelForm):
    class Meta:
        model=Olx
        fields="__all__"
        widgets ={
            "name":forms.TextInput(attrs={"class":"form-control"}),
            "brand":forms.TextInput(attrs={"class":"form-control"}),
            "modelyr":forms.TextInput(attrs={"class":"form-control"}),
            "types":forms.TextInput(attrs={"class":"form-control"}),
            "owner":forms.TextInput(attrs={"class":"form-control"}),
            "km":forms.TextInput(attrs={"class":"form-control"}),
            "price":forms.TextInput(attrs={"class":"form-control"}),
        }

