from django import forms
from principal.models import Adress

class Adress_form(forms.ModelForm):
    
    class Meta:
        model = Adress
        exclude = ('id_cliente',)
