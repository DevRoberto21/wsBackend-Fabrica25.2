from django.db import models
from django.core.validators import RegexValidator
class Pessoa(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    telefone = models.CharField(
        max_length=9,
        validators=[
            RegexValidator(
                regex=r'^9\d{8}$',
                message='O telefone deve começar com 9 e conter exatamente 9 dígitos.',
                code='invalid_telefone'
            )
        ]
    )