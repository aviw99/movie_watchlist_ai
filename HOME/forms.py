from django import forms
from .models import UserProfileModel

class ProfileForm(forms.ModelForm):
    class Meta():
        model = UserProfileModel
        fields = '__all__'
        widgets = {'user': forms.HiddenInput()}