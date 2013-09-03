from django import forms
from django.forms import ModelForm
from models import Question, Response, User

class ResponseForm(forms.Form):
    response = forms.CharField()

class UserForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.CharField()
    address = forms.CharField()
    city = forms.CharField()
    state = forms.CharField()
    country = forms.CharField()
    age = forms.CharField()
    gender = forms.CharField()

class UserModelForm(ModelForm):
    class Meta:
        model = User
