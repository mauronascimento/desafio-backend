from django.contrib import admin

from .models import Viagem

class ViagemAdmin(admin.ModelAdmin):
    list_display = (
        'customer', 'data_inicio', 'data_fim', 'classificacao', 'nota'
    )

admin.site.register(Viagem, ViagemAdmin)
