from django import forms
from .models import Cadastroitens



class CadastroitensForm(forms.ModelForm):
    class Meta:
     model = Cadastroitens
     fields = '__all__'
    #  widgets = {
    # #         'modelo': forms.Select(attrs={'class': 'form-control'})
    #  }
