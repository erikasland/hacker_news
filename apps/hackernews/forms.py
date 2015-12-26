from django import forms

class Registration(forms.Form):
    username = forms.CharField(label='Username', max_length=255, min_length=4)
    email = forms.CharField(label='Email', min_length=3, max_length=255)
    password = forms.CharField(widget=forms.PasswordInput, label='Password', max_length=255, min_length=8)
    confirm = forms.CharField(widget=forms.PasswordInput, label='Confirm Password', min_length=4, max_length=255)

class Login(forms.Form):
    username = forms.CharField(label='Username', min_length=4, max_length=255)
    password = forms.CharField(widget=forms.PasswordInput, label='Password', min_length=4, max_length=255)
    
class Search(forms.Form):
    search = forms.CharField(label='Search', max_length=255)