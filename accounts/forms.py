from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import CustomUser, UserProfile


class ProfileForm(forms.ModelForm):
    class Meta:
        Model = UserProfile
        fields = '__all__'
        widgets = {'user': forms.HiddenInput()}


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = '__all__'
