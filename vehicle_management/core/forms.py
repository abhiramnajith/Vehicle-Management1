from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Vehicle,Users

class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        exclude = ('updated_at','created_at','active_status')

class RegistrationForm(UserCreationForm):

    class Meta:
        model = Users
        fields = ['username', 'email', 'password1', 'password2','user_type']
