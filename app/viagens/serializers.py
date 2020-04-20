from rest_framework import serializers

from .models import Viagem


class ViagemSerializer(serializers.ModelSerializer):
    data_inicio = serializers.DateTimeField(source='data_inicio')
    data_fim = serializers.DateTimeField(source='data_fim')
    classificacao = serializers.IntegerField(source='classificacao')
    nota = serializers.IntegerField(source='nota')

    class Meta:
        model = Viagem
        fields = ('id', 'data_inicio', 'data_fim', 'classificacao', 'nota')


class ViagemNotaUpdateSerializer(serializers.ModelSerializer):
    classificacao = serializers.ChoiceField(
        source='classificacao', choices=Viagem.Classificacao.choices
    )
    nota = serializers.IntegerField(source='nota', min_value=1, max_value=5)

    class Meta:
        model = Viagem
        fields = ('id', 'classificacao', 'nota')
