from django.db import models

# Create your models here.
class Aluno(models.Model):
    nome = models.CharField('nome', max_length=50)
    telefone = models.CharField('telefone', max_length=15)

    def __str__(self):
        return f'Aluno: {self.nome}, Telefone: {self.telefone}'

# Create your models here.
class Aula(models.Model):
    nome = models.CharField('nome', max_length=50)

    def __str__(self):
        return f'Aula de: {self.nome}'

class Registro(models.Model):

    data = models.DateField('data')  
    aula = models.ForeignKey(Aula, on_delete=models.CASCADE)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    
    s = 'Sim'
    n = 'Não'
    
    falta = models.CharField(
        max_length=3,
        choices=[(s, 'Sim'),(n, 'Não')],
        default=n,
    )
    def __str__(self):
        return f'Registro do dia {self.data}, da aula de {self.aula} e do aluno: {self.aluno}'