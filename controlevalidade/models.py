
from django.db import models
from django.contrib.auth import get_user_model


class Cadastroitens(models.Model):
    produto = models.CharField('Produto', max_length=50)
    fornecedor = models.CharField('Fornecedor', max_length=70)
    lote = models.CharField('Lote', max_length=10)
    validade = models.DateField('Validade')
   
    


    def __str__(self):
        return self.produto

class Funcionario(models.Model):
    nome = models.CharField('Nome', max_length=100)
    funcao = models.CharField('Função', max_length=100)
    setor = models.CharField('Setor', max_length=100)
    
    
    def __str__(self):
        return self.nome
