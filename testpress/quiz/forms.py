from django import forms
from django.core import validators
from quiz.models import Users

class UsersForm(forms.ModelForm):
    
    class Meta():
        model=Users
        fields=('role','name','password')
    widgets={
           'password': forms.PasswordInput(),
    }
    def clean(self):
        all_clean_data=super().clean()
        password=all_clean_data['password']

        if len(password)<8:
            raise forms.ValidationError("please provide a password with more than 8 characters")
    
