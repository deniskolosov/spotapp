from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from shop.forms import SignUpForm


def index(request):
    """View function for home page of site."""

    return render(request, 'index.html')


def signup(request):
    form = SignUpForm(request.POST)
    if form.is_valid():
        user = form.save()
        user.refresh_from_db()
        user.customer.name = form.cleaned_data.get('name')
        user.customer.email = form.cleaned_data.get('email')
        user.save()
        password = form.cleaned_data.get('password1')
        username = form.cleaned_data.get('username')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
