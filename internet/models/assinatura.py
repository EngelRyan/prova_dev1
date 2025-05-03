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
    download = models.IntegerField(validators=[MinValueValidator(10), MaxValueValidator(10000)])
    upload = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10000)])
    franquia_dados = models.IntegerField(validators=[MinValueValidator(50)])
    fidelidade = models.DateField(validators=[validate_min_date_today])
    habilitado = models.BooleanField()
    contratacao = models.DateField(default=timezone.now)

    def validate_max_plano(self):
        # Define limites máximos para cada tipo de plano
        limites = {
            'BAS': {'download': 100, 'upload': 100},
            'STAND': {'download': 1000, 'upload': 1000},
            'PREM': {'download': 5000, 'upload': 5000},
            'MAS': {'download': 10000, 'upload': 10000},
        }

        # Verifica se o tipo da assinatura está nos limites definidos
        if self.tipo in limites:
            max_download = limites[self.tipo]['download']
            max_upload = limites[self.tipo]['upload']

            # Validação dos limites
            if self.download > max_download or self.upload > max_upload:
                raise ValidationError(
                    f"Para o tipo {self.tipo}, os limites são:"
                    f" download <= {max_download} e upload <= {max_upload}.",
                    params={"tipo": self.tipo, "download": self.download, "upload": self.upload}
                )
        else:
            raise ValidationError(
                f"O tipo de assinatura '{self.tipo}' não é válido.",
                params={"tipo": self.tipo}
            )

    def clean(self):
        self.validate_max_plano()
        super().clean()


    def __str__(self):
        return f'{self.owner} | {self.tipo}'
