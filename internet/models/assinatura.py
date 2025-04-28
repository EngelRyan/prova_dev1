from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator
from django.db.models import CASCADE
from django.utils import timezone
from .base_model import BaseModel
from django.db import models

from ..enumerations.tipo_plano import TipoPlano
from .cliente import Cliente


class Assinatura(BaseModel):
    owner = models.OneToOneField(Cliente,on_delete=CASCADE)
    tipo = models.CharField(max_length=10, null=False, blank=False,choices=TipoPlano, default=TipoPlano.STANDARD,)
    descricao = models.CharField(max_length=200, validators=[MinLengthValidator(20)], blank=True, null=True)
    mensalidade = models.DecimalField( max_digits=6, decimal_places=2,  validators=[MinValueValidator(0.00)])
    donwload = models.IntegerField(validators=[MinValueValidator(10), MaxValueValidator(10000)])
    upload = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10000)])
    franquia_dados = models.IntegerField(validators=[MinValueValidator(50)])
    fidelidade = models.DateField(validators=[MinValueValidator(timezone.datetime.date(timezone.now()))])
    habilitado = models.BooleanField()
    contratacao = models.DateField(default=timezone.now)


    def __str__(self):
        return f'{self.owner} | {self.tipo}'
