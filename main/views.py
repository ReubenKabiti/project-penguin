from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import django.contrib.auth as auth
from .models import User
from . import forms

def index(req):
    if not req.user.is_authenticated:
        return HttpResponseRedirect("login/")
    else:
        return render(req, "index.html", {})

def login(req):

    if req.method == "GET":
        return render(req, "login.html", {
            "login_form" : forms.LoginForm(),
        })
    else:

        form = forms.LoginForm(req.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = auth.authenticate(username=username, password=password)

            if user == None:
                return HttpResponseRedirect("/login/")

            auth.login(req, user)
            return HttpResponseRedirect("/")

def signup(req):

    html_data = {}

    if req.method == "GET":
        return render(req, "signup.html", {
            "signup_form" : forms.UserCreationForm(),
        })
    else:
        form = forms.UserCreationForm(req.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            try:
                User.objects.get(username=username)
                return HttpResponseRedirect("/signup/")
            except:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                auth.login(req, user)
                return HttpResponseRedirect("/")
        else:
            return HttpResponseRedirect("/signup/")
