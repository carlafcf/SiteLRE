from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from Pesquisador.models import Pesquisador

# Create your models here.
class Artigo (models.Model):
    titulo = models.CharField(max_length=1000, null=False, blank=False, verbose_name="Título")
    ano = models.IntegerField(
        validators=[
            MaxValueValidator(2200),
            MinValueValidator(1900)
        ], null=False, blank=False, verbose_name="Ano da publicação")
    publicacao = models.CharField(max_length=1000, null=False, blank=False, verbose_name="Publicação")

    palavras_chave = models.CharField(max_length=1000, null=False, blank=False, verbose_name="Palavras-chave")
    resumo = models.TextField(verbose_name="Resumo")
    abstract = models.TextField(verbose_name="Abstract")

    autores = models.ManyToManyField(Pesquisador)

    link = models.URLField(verbose_name="Link da publicação")
    # imagem

    def __str__(self) -> str:
        return self.titulo

    class Meta:
        verbose_name = "Artigo"
        verbose_name_plural = "Artigos"