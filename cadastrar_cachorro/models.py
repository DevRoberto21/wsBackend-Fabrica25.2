from django.db import models
from django.core.validators import MaxValueValidator
class Cachorro(models.Model):
   dono = models.ForeignKey(
      'cadastrar_pessoa.Pessoa',
      on_delete=models.CASCADE,
      related_name='cachorros',
   )
   nome = models.CharField(max_length=50)
   raca = models.CharField(max_length=50)
   idade = models.IntegerField(
     validators=[
        MaxValueValidator(
           20, message='A idade do cachorro não pode ser maior 20 anos, por questão de risco.'
        )
     ]
   )
