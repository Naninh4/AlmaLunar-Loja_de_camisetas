from socket import fromshare
from django import forms
from principal.models import *

class User_form(forms.ModelForm):
    class Meta:
        model: User
        fields: '__all__'
        
class Adress_form(forms.ModelForm):
    
    class Meta:
        model: Adress
        fields: '__all__'


