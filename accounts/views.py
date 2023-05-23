from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from .forms import SignupForm
from .models import UserProfile
from django.contrib.auth.models import User


class signupView(generic.CreateView):
    form_class = SignupForm
    success_url = reverse_lazy('homepage')
    template_name = 'signup.html'


class profile_view(generic.DetailView):
    model = User
    template_name = 'profile.html'
    context_object_name = 'profile'
