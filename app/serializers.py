from rest_framework import serializers
from .models import TipoBacia, Engenheiro, Bacia


class TipoBaciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoBacia
        fields = ['id', 'nome']


class EngenheiroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Engenheiro
        fields = ['id', 'nome', 'cpf', 'crea']


class BaciaSerializer(serializers.ModelSerializer):
    tipoBacia = TipoBaciaSerializer()
    engenheiro = EngenheiroSerializer()

    class Meta:
        model = Bacia
        fields = ['id', 'tipoBacia', 'profundidade', 'capacidade', 'largura', 'comprimento', 'engenheiro']