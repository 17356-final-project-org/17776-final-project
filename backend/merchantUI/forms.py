from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))

    def clean(self):
        clean_data = super().clean()
        username = clean_data['username']
        password = clean_data['password']

        user = authenticate(username=username, password=password)
        if not user:
            raise forms.ValidationError('Invalid username or password.')

        return clean_data

class RegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}))

    def clean(self):
        clean_data = super().clean()

        # Verify that passwords match.
        pwd1 = clean_data['password']
        pwd2 = clean_data['confirm_password']
        if pwd1 and pwd2 and pwd1 != pwd2:
            raise forms.ValidationError("Passwords do not match.")

        # Verify that username is unique.
        username = clean_data['username']
        if User.objects.all().filter(username__exact=username):
            raise forms.ValidationError("Username already exists.")

        return clean_data

class ItemUploadForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Item Name'}))
    nominalPrice = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Nominal Price'}))
    lowestPrice = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Lowest Price'}))
    itemUrl = forms.URLField(widget=forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Item URL'}))