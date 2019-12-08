from django import forms
from django.contrib.auth.forms import UserCreationForm


class CustomerForm(UserCreationForm):
    email = forms.EmailField()
    name = forms.CharField()
