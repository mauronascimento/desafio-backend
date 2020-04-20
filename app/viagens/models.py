from django.db import models
from django.utils.translation import ugettext_lazy as _


class Viagem(models.Model):

    class Classificacao(models.IntegerChoices):
        WORK = 1, _('work')
        PHYSICAL_ACTIVITY = 2, _('physical activity')
        RECREATION = 3, _('recreation')
        DISPLACEMENT = 4, _('displacement')


    customer = models.ForeignKey(
        'accounts.Customer',
        related_name='viagens',
        on_delete=models.CASCADE
    )
    data_inicio = models.DateTimeField(
        _('data_inicio')
    )
    data_fim = models.DateTimeField(
        _('data_fim')
    )
    nota = models.PositiveIntegerField(
        _('nota'),
        blank=True,
        null=True
    )
    classificacao = models.IntegerField(
        _('classificacao'),
        choices=Classificacao.choices,
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = _('viagem')
        verbose_name_plural = _('viagens')

    def __str__(self):
        return self.customer.name
