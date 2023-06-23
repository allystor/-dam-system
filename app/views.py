from django.shortcuts import render

from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.forms import UserCreationForm
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import *
from .serializers import BaciaSerializer
from .form import *

# Gerenciamento --------------------------------------------------------------------------------------------------------


def gerenciamento(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'gerenciamento.html')

# Engenheiro -----------------------------------------------------------------------------------------------------------

def engenheiro_list(request):
    if not request.user.is_authenticated:
        return redirect('login')
    items = Engenheiro.objects.order_by('-id')
    return render(request, 'engenheiro.html', {'items': items})


def engenheiro_create(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == 'POST':
        form = EngenheiroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(engenheiro_list)  # Ajuste o nome da rota se necessário
    else:
        form = EngenheiroForm()
    return render(request, 'engenheiro_form.html', {'form': form})


def engenheiro_edit(request, id):
    if not request.user.is_authenticated:
        return redirect('login')
    engenheiro = Engenheiro.objects.get(id=id)
    if request.method == 'POST':
        form = EngenheiroForm(request.POST, instance=engenheiro)
        if form.is_valid():
            form.save()
            return redirect(engenheiro_list)  # Ajuste o nome da rota se necessário
    else:
        form = EngenheiroForm(instance=engenheiro)
    return render(request, 'engenheiro_form.html', {'form': form})

# Endereco -------------------------------------------------------------------------------------------------------------


def endereco_list(request):
    if not request.user.is_authenticated:
        return redirect('login')
    items = Endereco.objects.order_by('-id')
    return render(request, 'enderecos.html', {'items': items})


def endereco_create(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == 'POST':
        form = EnderecoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(endereco_list)  # Ajuste o nome da rota se necessário
    else:
        form = EnderecoForm()
    return render(request, 'endereco_form.html', {'form': form})


def endereco_edit(request, id):
    if not request.user.is_authenticated:
        return redirect('login')
    endereco = Endereco.objects.get(id=id)
    if request.method == 'POST':
        form = EnderecoForm(request.POST, instance=endereco)
        if form.is_valid():
            form.save()
            return redirect(endereco_list)  # Ajuste o nome da rota se necessário
    else:
        form = EnderecoForm(instance=endereco)
    return render(request, 'endereco_form.html', {'form': form})

# Tipo Bacias ----------------------------------------------------------------------------------------------------------


def tipo_bacia_list(request):
    if not request.user.is_authenticated:
        return redirect('login')
    items = TipoBacia.objects.order_by('-id')
    return render(request, 'tipo_bacias.html', {'items': items})


def tipo_bacia_create(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == 'POST':
        form = TipoBaciaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(tipo_bacia_list)
    else:
        form = TipoBaciaForm()
    return render(request, 'tipo_bacia_form.html', {'form': form})


def tipo_bacia_edit(request, id):
    if not request.user.is_authenticated:
        return redirect('login')
    tipo_bacia = TipoBacia.objects.get(id=id)
    if request.method == 'POST':
        form = TipoBaciaForm(request.POST, instance=tipo_bacia)
        if form.is_valid():
            form.save()
            return redirect(tipo_bacia_list)
    else:
        form = TipoBaciaForm(instance=tipo_bacia)
    return render(request, 'tipo_bacia_form.html', {'form': form})

# Bacias View ----------------------------------------------------------------------------------------------------------


def bacias_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    bacias = Bacia.objects.all()
    data = {
        'bacias': []
    }
    for bacia in bacias:
        data['bacias'].append({
            'tipoBacia': bacia.tipoBacia.nome,
            'profundidade': bacia.profundidade,
            'capacidade': bacia.capacidade,
            'largura': bacia.largura,
            'comprimento': bacia.comprimento,
            'engenheiro': bacia.engenheiro.nome,
        })
    return JsonResponse(data)


class BaciaList(APIView):
    def get(self, request):
        bacias = Bacia.objects.all()
        serializer = BaciaSerializer(bacias, many=True)
        return Response(serializer.data)


def bacia_list(request):
    if not request.user.is_authenticated:
        return redirect('login')
    items = Bacia.objects.all()
    return render(request, 'bacias.html', {'items': items})


def bacia_create(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == 'POST':
        form = BaciaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bacias')
    else:
        form = BaciaForm()
    return render(request, 'bacia_form.html', {'form': form})


def bacia_edit(request, id):
    if not request.user.is_authenticated:
        return redirect('login')
    item = Bacia.objects.get(pk=id)
    if request.method == 'POST':
        form = BaciaForm(request.POST, instance=item)
        if 'excluir' in request.POST:
            item.delete()
            return redirect('bacias')
        if form.is_valid():
            form.save()
            return redirect('bacias')
    else:
        form = BaciaForm(instance=item)
    return render(request, 'bacia_form.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('gerenciamento')
            else:
                error_message = 'Nome de usuário ou senha inválidos.'
                return render(request, 'login.html', {'form': form, 'error_message': error_message})
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def user_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('gerenciamento')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')