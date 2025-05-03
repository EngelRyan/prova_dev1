import os
import sys
import django
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from django.utils import timezone
from internet.models.cliente import Cliente
from internet.models.assinatura import Assinatura
from internet.enumerations.tipo_plano import TipoPlano

# Configuração do Django
sys.path.append('C:\\Users\\Windows 10 Pro\\OneDrive\\Área de Trabalho\\Scripts\\prova_dev1')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sulnet.settings')
django.setup()

# Criação do superusuário
User = get_user_model()
User.objects.create_superuser('ifrs', 'admin@myproject.com', 'ifrs')


# Função para criar clientes
def criar_cliente(nome, cpf, endereco, cidade, estado, telefone, email, ativo):
    try:
        cliente = Cliente(
            nome=nome,
            cpf=cpf,
            endereco=endereco,
            cidade=cidade,
            estado=estado,
            telefone=telefone,
            email=email,
            ativo=ativo,
        )
        cliente.full_clean()
        cliente.save()
        return cliente
    except ValidationError as e:
        print(f"Erro ao criar cliente {nome}: {e.message_dict}")
        return None


# Função para criar assinaturas
def criar_assinatura(owner, tipo, descricao, mensalidade, download, upload, franquia_dados):
    try:
        assinatura = Assinatura(
            owner=owner,
            tipo=tipo,
            descricao=descricao,
            mensalidade=mensalidade,
            download=download,  # Corrigido aqui
            upload=upload,
            franquia_dados=franquia_dados,
            fidelidade=timezone.now() + timezone.timedelta(days=30),  # Data futura
            habilitado=True,
            contratacao=timezone.now(),
        )
        assinatura.full_clean()
        assinatura.save()
        return assinatura
    except ValidationError as e:
        print(f"Erro ao criar assinatura para o cliente {owner.nome}: {e.message_dict}")
        return None


ryan = criar_cliente('Ryan Engel', '11111111111', 'rua ksksks', 'porto alegre', 'rs', '545454545454', 'ryan@mail.com',
                     True)
edu = criar_cliente('Edusasaas K.', '22222222222', 'rua edu', 'porto edu', 'rs', '8794562132186', 'edu@mail.com', False)
pedro = criar_cliente('pedrooooooo', '33333333333', 'rua fdsffsffsd', 'porto pedrooooo', 'rs', '634555435435',
                      'pedroooo@mail.com', True)

if ryan:
    criar_assinatura(ryan, TipoPlano.STANDARD, 'Standard Plan', 500, 152, 200, 500)
if edu:
    criar_assinatura(edu, TipoPlano.PREMIUM, 'Premium Plan', 800, 300, 400, 1000)
if pedro:
    criar_assinatura(pedro, TipoPlano.MASTER, 'Master Plan', 1200, 1000, 800, 2000)
