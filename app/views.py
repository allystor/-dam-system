from django.shortcuts import render

from django.shortcuts import render, redirect
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.decorators import login_required

from .models import *
from .serializers import BaciaSerializer
from .form import *

# Gerenciamento --------------------------------------------------------------------------------------------------------

@login_required
def gerenciamento(request):
    return render(request, 'gerenciamento.html')

# Engenheiro -----------------------------------------------------------------------------------------------------------

@login_required
def engenheiro_list(request):
    items = Engenheiro.objects.order_by('-id')
    return render(request, 'engenheiro.html', {'items': items})
@login_required
def engenheiro_create(request):
    if request.method == 'POST':
        form = EngenheiroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(engenheiro_list)  # Ajuste o nome da rota se necessário
    else:
        form = EngenheiroForm()
    return render(request, 'engenheiro_form.html', {'form': form})
@login_required
def engenheiro_edit(request, id):
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

@login_required
def endereco_list(request):
    items = Endereco.objects.order_by('-id')
    return render(request, 'enderecos.html', {'items': items})

@login_required
def endereco_create(request):
    if request.method == 'POST':
        form = EnderecoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(endereco_list)  # Ajuste o nome da rota se necessário
    else:
        form = EnderecoForm()
    return render(request, 'endereco_form.html', {'form': form})

@login_required
def endereco_edit(request, id):
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

@login_required
def tipo_bacia_list(request):
    items = TipoBacia.objects.order_by('-id')
    return render(request, 'tipo_bacias.html', {'items': items})
@login_required

def tipo_bacia_create(request):
    if request.method == 'POST':
        form = TipoBaciaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(tipo_bacia_list)
    else:
        form = TipoBaciaForm()
    return render(request, 'tipo_bacia_form.html', {'form': form})

@login_required()
def tipo_bacia_edit(request, id):
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

@login_required
def bacias_view(request):
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

@login_required
class BaciaList(APIView):
    def get(self, request):
        bacias = Bacia.objects.all()
        serializer = BaciaSerializer(bacias, many=True)
        return Response(serializer.data)

@login_required
def bacia_list(request):
    items = Bacia.objects.all()
    return render(request, 'bacias.html', {'items': items})

@login_required
def bacia_create(request):
    if request.method == 'POST':
        form = BaciaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bacias')
    else:
        form = BaciaForm()
    return render(request, 'bacia_form.html', {'form': form})

@login_required
def bacia_edit(request, id):
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
