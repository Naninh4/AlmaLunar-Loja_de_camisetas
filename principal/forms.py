from socket import fromshare
from django import forms
from principal.models import Cliente

class Cliente_form(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__' # selecionando todos os campos do model
