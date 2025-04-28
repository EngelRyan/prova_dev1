from django.core.validators import MinLengthValidator

from .base_model import BaseModel
from django.db import models


class Cliente(BaseModel):
    nome = models.CharField(max_length=100, validators=[MinLengthValidator(10)])
    cpf = models.CharField(max_length=11, validators=[MinLengthValidator(11)], unique=True)
    endereco = models.CharField(max_length=100, validators=[MinLengthValidator(20)])
    cidade = models.CharField(max_length=50, validators=[MinLengthValidator(3)])
    estado = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    telefone = models.CharField(max_length=20, validators=[MinLengthValidator(10)])
    email = models.EmailField(max_length=100, validators=[MinLengthValidator(10)])
    ativo = models.BooleanField(default=True)


    def __str__(self):
        return self.nome