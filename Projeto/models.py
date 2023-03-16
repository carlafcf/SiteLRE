from django.db import models
from datetime import date

from Pesquisador.models import Pesquisador

# Create your models here.
class Projeto (models.Model):
    titulo = models.CharField(max_length=1000, null=False, blank=False, verbose_name="Título")
    descricao = models.TextField(null=False, blank=False, verbose_name="Descrição")
    data_inicio = models.DateField(default=date.today, null=False, blank=False, verbose_name="Data de início")
    data_fim = models.DateField(default=date.today, verbose_name="Data de fim")

    participantes = models.ManyToManyField(Pesquisador, through='Participacao')
    # imagem

    def __str__(self) -> str:
        return self.titulo

    # class Meta:
        # ordering

class Participacao(models.Model):
    pesquisador = models.ForeignKey(Pesquisador, on_delete=models.RESTRICT)
    projeto = models.ForeignKey(Projeto, on_delete=models.RESTRICT)
    data_entrada = models.DateField(default=date.today, verbose_name='Data de entrada')
    ativo = models.BooleanField(default=True, null=False, blank=False, verbose_name="Ativo")
