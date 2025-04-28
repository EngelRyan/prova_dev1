from django.utils.translation import gettext_lazy as _
from django.db import models

class TipoPlano(models.TextChoices):
    BASIC = "BAS", _("Básico")
    STANDARD = "STAND", _("Padrão")
    PREMIUM = "PREM", _("Premium")
    MASTER = "MAS", _("Master")
