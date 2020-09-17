# from django import forms

# class NameForm(forms.Form):
#     your_name = forms.CharField(label='Your name', max_length=100)

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import *
from myapp.models import UserProfileInfo

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
class jobdata(ModelForm):
    class Meta:
        model = jobseaker_login
        exclude = () 

class companydata(ModelForm):
    class Meta:
        model = company_login
        exclude = () 



class logidata(ModelForm):
    class Meta:
        model = logi
        exclude = () 

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','password','email')
class UserProfileInfoForm(forms.ModelForm):
     class Meta():
         model = UserProfileInfo
         fields = ('portfolio_site','profile_pic')