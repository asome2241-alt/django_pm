from django import forms
from django.contrib.auth.forms import AuthenticationForm

attrs = {
    'class': 'form-control',
    'placeholder': 'Username'
}  

class LoginForm(AuthenticationForm):

    username = forms.CharField(
        widget=forms.TextInput(
            attrs=attrs
        )
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Password'
            }
        )
    )