from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from newoperation.models import OlxNew


class RegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=["username","email","password1","password2"]

class LoginForm(forms.Form):
    username =forms.CharField()
    password =forms.CharField()

class OlxnewCreateForm(forms.ModelForm):
    class Meta:
        model = OlxNew
        fields=["name","brand","modelyr","types","owner","km","price","image"]


class OlxNewChangeForm(forms.ModelForm):
    class Meta:
        model= OlxNew
        fields=["name","brand","modelyr","types","owner","km","price","image"]


