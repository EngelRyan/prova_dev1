from django.contrib import admin
from .models.cliente import Cliente
from .models.assinatura import Assinatura

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Assinatura)
