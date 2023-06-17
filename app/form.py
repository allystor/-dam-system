from django import forms
from .models import *

class TipoBaciaForm(forms.ModelForm):
    class Meta:
        model = TipoBacia
        fields = ['nome']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
        }


class EngenheiroForm(forms.ModelForm):
    class Meta:
        model = Engenheiro
        fields = ['nome', 'cpf', 'crea']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control'}),
            'crea': forms.TextInput(attrs={'class': 'form-control'}),
        }


class EnderecoForm(forms.ModelForm):
    class Meta:
        model = Endereco
        fields = ['rua', 'numero', 'bairro', 'cidade', 'estado', 'cep']
        widgets = {
            'rua': forms.TextInput(attrs={'class': 'form-control'}),
            'numero': forms.NumberInput(attrs={'class': 'form-control'}),
            'bairro': forms.TextInput(attrs={'class': 'form-control'}),
            'cidade': forms.TextInput(attrs={'class': 'form-control'}),
            'estado': forms.TextInput(attrs={'class': 'form-control'}),
            'cep': forms.TextInput(attrs={'class': 'form-control'}),
        }

class BaciaForm(forms.ModelForm):
    class Meta:
        model = Bacia
        fields = ['tipoBacia', 'endereco', 'profundidade', 'capacidade', 'largura', 'comprimento', 'engenheiro']
        widgets = {
            'tipoBacia': forms.TextInput(attrs={'class': 'form-control'}),
            'endereco': forms.TextInput(attrs={'class': 'form-control'}),
            'profundidade': forms.NumberInput(attrs={'class': 'form-control'}),
            'capacidade': forms.NumberInput(attrs={'class': 'form-control'}),
            'largura': forms.NumberInput(attrs={'class': 'form-control'}),
            'comprimento': forms.NumberInput(attrs={'class': 'form-control'}),
            'engenheiro': forms.TextInput(attrs={'class': 'form-control'}),
        }
