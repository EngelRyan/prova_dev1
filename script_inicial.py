from .internet.models.cliente import Cliente
from .internet.models.assinatura import Assinatura
from .internet.enumerations.tipo_plano import TipoPlano
from django.contrib.auth import get_user_model
from django.utils import timezone


User = get_user_model()
User.objects.create_superuser('ifrs','admin@myproject.com','ifrs')

ryan = Cliente(
    nome = 'Ryan Engel kskssk',
    cpf = '11111111111',
    endereco = 'rua kskskskssksksksksdsd',
    cidade = 'porto alere kaka',
    estado = 'rs',
    telefone = '545454545454',
    email = 'ryanzinho@mail.com',
    ativo = True
)
ryan.full_clean()
ryan.save()

edu = Cliente(
    nome = 'edu edu kskssk',
    cpf = '99999999999',
    endereco = 'rua edu kskskskssksksksksdsd',
    cidade = 'porto edu kaka',
    estado = 'rs',
    telefone = '8794562132186',
    email = 'eduzinhomal@mail.com',
    ativo = False
)
edu.full_clean()
edu.save()

pedro = Cliente(
    nome = 'pedro pedro kskssk',
    cpf = '11111111111',
    endereco = 'rua pedro kskskskssksksksksdsd',
    cidade = 'porto pedro kaka',
    estado = 'rs',
    telefone = '879545564879',
    email = 'pedropedro@mail.com',
    ativo = True
)
pedro.full_clean()
pedro.save()

ric = Cliente(
    nome = 'ric ric kskssk',
    cpf = '11111111111',
    endereco = 'rua ric kskskskssksksksksdsd',
    cidade = 'porto ric kaka',
    estado = 'rs',
    telefone = '879545564879',
    email = 'ricricric@mail.com',
    ativo = True
)
ric.full_clean()
ric.save()

ardo = Cliente(
    nome = 'ardo ardo kskssk',
    cpf = '11111111111',
    endereco = 'rua ardo kskskskssksksksksdsd',
    cidade = 'porto ardo kaka',
    estado = 'rs',
    telefone = '879545564879',
    email = 'ardoardoardo@mail.com',
    ativo = True
)
ardo.full_clean()
ardo.save()

ass1 = Assinatura(
    owner = ryan,
    tipo = TipoPlano.STANDARD,
    descricao = 'fsaetadsfdsfdsfdsfads',
    mensalidade = 500,
    donwload = 152,
    upload = 200,
    franquia_dados = 500,
    fidelidade = timezone.now(),
    habilitado = True,
    contratacao = timezone.now()
)
ass1.full_clean()
ass1.save()

ass2 = Assinatura(
    owner = edu,
    tipo = TipoPlano.PREMIUM,
    descricao = 'fsaetadsfdsfdsfdsfads',
    mensalidade = 500,
    donwload = 152,
    upload = 200,
    franquia_dados = 500,
    fidelidade = timezone.now(),
    habilitado = True,
    contratacao = timezone.now()
)
ass2.full_clean()
ass2.save()

ass3 = Assinatura(
    owner = pedro,
    tipo = TipoPlano.MASTER,
    descricao = 'fsaetadsfdsfdsfdsfads',
    mensalidade = 500,
    donwload = 152,
    upload = 200,
    franquia_dados = 500,
    fidelidade = timezone.now(),
    habilitado = True,
    contratacao = timezone.now()
)
ass3.full_clean()
ass3.save()

ass4 = Assinatura(
    owner = ric,
    tipo = TipoPlano.STANDARD,
    descricao = 'fsaetadsfdsfdsfdsfads',
    mensalidade = 500,
    donwload = 152,
    upload = 200,
    franquia_dados = 500,
    fidelidade = timezone.now(),
    habilitado = True,
    contratacao = timezone.now()
)
ass4.full_clean()
ass4.save()

ass5 = Assinatura(
    owner = ardo,
    tipo = TipoPlano.STANDARD,
    descricao = 'fsaetadsfdsfdsfdsfads',
    mensalidade = 500,
    donwload = 152,
    upload = 200,
    franquia_dados = 500,
    fidelidade = timezone.now(),
    habilitado = True,
    contratacao = timezone.now()
)
ass5.full_clean()
ass5.save()

