from django.shortcuts import render

from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Bacia
from .serializers import BaciaSerializer


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

class BaciaList(APIView):
    def get(self, request):
        bacias = Bacia.objects.all()
        serializer = BaciaSerializer(bacias, many=True)
        return Response(serializer.data)