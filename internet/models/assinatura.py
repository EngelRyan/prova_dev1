from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator
from django.db.models import CASCADE
from django.utils import timezone
from .base_model import BaseModel
from django.db import models

from ..enumerations.tipo_plano import TipoPlano
from .cliente import Cliente
from ..validators.validators import validate_min_date_today


class Assinatura(BaseModel):
    owner = models.OneToOneField(Cliente,on_delete=CASCADE)
    tipo = models.CharField(max_length=10, null=False, blank=False,choices=TipoPlano, default=TipoPlano.STANDARD,)
    descricao = models.CharField(max_length=200, validators=[MinLengthValidator(20)], blank=True, null=True)
    mensalidade = models.DecimalField( max_digits=6, decimal_places=2,  validators=[MinValueValidator(0.00)])
    donwload = models.IntegerField(MinValueValidator(1), MaxValueValidator(10000))
    upload = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10000)])
    franquia_dados = models.IntegerField(validators=[MinValueValidator(50)])
    fidelidade = models.DateField(validators=[validate_min_date_today])
    habilitado = models.BooleanField()
    contratacao = models.DateField(default=timezone.now)

    def validate_max_plano(self):
        if self.tipo == 'Básico':
            self.donwload = models.IntegerField(validators=[MaxValueValidator(100)])
            self.upload = models.IntegerField(validators=[MaxValueValidator(100)])

        elif self.tipo == 'Padrão':
            self.donwload = models.IntegerField(validators=[MaxValueValidator(1000)])
            self.upload = models.IntegerField(validators=[MaxValueValidator(1000)])

        elif self.tipo == 'Premium':
            self.donwload = models.IntegerField(validators=[MaxValueValidator(5000)])
            self.upload = models.IntegerField(validators=[MaxValueValidator(5000)])

        elif self.tipo == 'Master':
            self.donwload = models.IntegerField(validators=[MaxValueValidator(10000)])
            self.upload = models.IntegerField(validators=[MaxValueValidator(10000)])

    def __str__(self):
        return f'{self.owner} | {self.tipo} | { type(self.fidelidade) }'
