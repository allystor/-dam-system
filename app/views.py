from django.shortcuts import render

from django.shortcuts import render
from django.http import JsonResponse
from .models import Bacia

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
