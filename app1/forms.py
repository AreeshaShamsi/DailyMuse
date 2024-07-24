from django import forms
from .models import app1
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class app1form(forms.ModelForm):
    class Meta:
        model = app1
        fields = ['text', 'photo']

class UserRegistrationForm(UserCreationForm):
    email=forms.EmailField()
    class Meta:
        model= User    
        fields=('username','email','password1','password2')    
