from django.urls import path, include
from django.contrib.auth import views as auth_views
from .forms import LoginForm
from .views import RegisterView, edit_profile

urlpatterns = [

    path(
        'login/',
        auth_views.LoginView.as_view(
            authentication_form=LoginForm
        ),
        name='login'
    ),

    path(
        'logout/',
        auth_views.LogoutView.as_view(),
        name='logout'
    ),

    path(
        'register/',
        RegisterView.as_view(),
        name='register'
    ),

    path(
        'profile/',
        edit_profile,
        name='profile'
    ),

]