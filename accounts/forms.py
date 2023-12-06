# accounts/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email']  # Customize this list based on your needs

class PasswordChangeCustomForm(PasswordChangeForm):
    pass
