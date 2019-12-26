from django import forms
from .models import UserModel

class RegisterForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = '__all__'