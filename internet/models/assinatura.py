from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator
from django.db.models import CASCADE
from django.utils import timezone
from .base_model import BaseModel
from django.db import models
from django.core.exceptions import ValidationError

from ..enumerations.tipo_plano import TipoPlano
from .cliente import Cliente
from ..validators.validators import validate_min_date_today


class Assinatura(BaseModel):
    owner = models.OneToOneField(Cliente,on_delete=CASCADE)
    tipo = models.CharField(max_length=10, null=False, blank=False,choices=TipoPlano, default=TipoPlano.STANDARD,)
    descricao = models.CharField(max_length=200, validators=[MinLengthValidator(20)], blank=True, null=True)
    mensalidade = models.DecimalField( max_digits=6, decimal_places=2,  validators=[MinValueValidator(0.00)])
    donwload = models.IntegerField(validators=[MinValueValidator(10), MaxValueValidator(10000)])
    upload = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10000)])
    franquia_dados = models.IntegerField(validators=[MinValueValidator(50)])
    fidelidade = models.DateField(validators=[validate_min_date_today])
    habilitado = models.BooleanField()
    contratacao = models.DateField(default=timezone.now)

    def validate_max_plano(self):
        if self.tipo == 'Básico' and self.donwload > 100 and self.upload > 100:
            raise ValidationError(
                "não pode > 100",
                params={"tipo": self.tipo}
            )

        elif self.tipo == 'Padrão' and self.donwload > 1000 and self.upload > 1000:
            raise ValidationError(
                "não pode > 1000",
                params={"tipo": self.tipo}
            )

        elif self.tipo == 'Premium' and self.donwload > 5000 and self.upload > 5000:
            raise ValidationError(
                "não pode > 5000",
                params={"tipo": self.tipo}
            )

        elif self.tipo == 'Master' and self.donwload > 10000 and self.upload > 10000:
            raise ValidationError(
                "não pode > 10000",
                params={"tipo": self.tipo}
            )


    def __str__(self):
        return f'{self.owner} | {self.tipo}'
