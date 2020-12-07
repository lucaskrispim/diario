from django import forms

from .models import Aluno,Aula,Registro

class AlunoModelForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ['nome','telefone']


class AulaModelForm(forms.ModelForm):
    class Meta:
        model = Aula
        fields = ['nome']

class RegistroModelForm(forms.ModelForm):
    class Meta:
        model = Registro
        fields = ['data','aula','aluno','falta']

class RegistroBuscaModelForm(forms.ModelForm):
    class Meta:
        model = Registro
        fields = ['aula','data']        

