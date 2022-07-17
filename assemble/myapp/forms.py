from django import forms
from .models import myUser

class UserModelForm(forms.ModelForm):
    class Meta:
        model = myUser
        fields = '__all__'