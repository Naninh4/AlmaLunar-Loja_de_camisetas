from socket import fromshare
from django import forms
from principal.models import *

class Adress_form(forms.ModelForm):
    
    class Meta:
        model = Adress
        fields = '__all__'

