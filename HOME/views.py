from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic import CreateView, DetailView
from .models import UserProfileModel
from .forms import ProfileForm
from django.contrib.auth import login
import requests
from django.urls import reverse_lazy
# Create your views here.
class signup_view(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'register.html'

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('homepage.html')
        else:
            form = AuthenticationForm()
        return render(request, 'start.html', {'form': form})

def homepage_view(request):
    return render(request, 'homepage.html')

 