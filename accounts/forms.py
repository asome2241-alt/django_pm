from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


attrs = {
    'class': 'form-control'
}


class LoginForm(AuthenticationForm):

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Username'
            }
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


class UserRegisterForm(UserCreationForm):

    first_name = forms.CharField(
        label='First Name',
        widget=forms.TextInput(attrs=attrs)
    )

    last_name = forms.CharField(
        label='Last Name',
        widget=forms.TextInput(attrs=attrs)
    )

    username = forms.CharField(
        label='Username',
        widget=forms.TextInput(attrs=attrs)
    )

    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs=attrs)
    )

    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs=attrs)
    )

    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(attrs=attrs)
    )

    class Meta:

        model = User

        fields = (
            'first_name',
            'last_name',
            'username',
            'email',
            'password1',
            'password2'
        )


class ProfileForm(forms.ModelForm):

    first_name = forms.CharField(
        widget=forms.TextInput(attrs=attrs)
    )

    last_name = forms.CharField(
        widget=forms.TextInput(attrs=attrs)
    )

    username = forms.CharField(
        widget=forms.TextInput(attrs=attrs)
    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs=attrs)
    )

    class Meta:

        model = User

        fields = (
            'first_name',
            'last_name',
            'username',
            'email'
        )