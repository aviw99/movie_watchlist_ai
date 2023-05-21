from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import homepage_view, signup_view, login_view

urlpatterns = [
    path('homepage/', homepage_view, name='homepage'),
    path('signup/', signup_view.as_view(), name='signup'),
    
    path('login/', login_view, name='login'),

    
]