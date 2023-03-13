from django import forms

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(min_length=6, max_length=16)

class UserCreationForm(forms.Form):
    username = forms.CharField(max_length=20)
    email = forms.EmailField()
    password = forms.CharField(min_length=6, max_length=16)
