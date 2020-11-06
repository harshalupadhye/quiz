from django import forms
from django.core import validators
from quiz.models import Users
from django.contrib.auth.models import User

class UsersForm(forms.ModelForm):
    # password=forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model=Users
        fields=('role','name','password')
   
    
    def clean(self):
        all_clean_data=super().clean()
        password=all_clean_data['password']

        if len(password)<8:
            raise forms.ValidationError("please provide a password with more than 8 characters")
    
