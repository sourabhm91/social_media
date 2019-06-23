from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

class SignInForm(forms.Form):
    username = forms.CharField(required=True, label="User Name")
    password = forms.CharField(required=True, label="Password",
                               widget=forms.PasswordInput())

    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user is None:
            raise forms.ValidationError("username or password is invalid")

class SignUpForm(forms.Form):
    email = forms.EmailField(required=True, label="Email")
    username = forms.CharField(required=True, label="User Name")
    password = forms.CharField(
        required=True,
        label='Password',
        widget=forms.PasswordInput()
    )

    def clean(self):
        cleaned_data = self.cleaned_data
        if User.objects.filter(username=cleaned_data.get('username')).exists():
            raise forms.ValidationError('Looks like a username with that email or password already exists')