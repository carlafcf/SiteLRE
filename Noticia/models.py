from django.db import models
from datetime import date

# Create your models here.
class Noticia (models.Model):
    titulo = models.CharField(max_length=1000, null=False, blank=False, verbose_name="Título")
    texto = models.TextField(null=False, blank=False, verbose_name="Texto")
    data = models.DateField(default=date.today, null=False, blank=False, verbose_name="Data")
    # imagem

    def __str__(self) -> str:
        return self.titulo

    class Meta:
        verbose_name = "Notícia"
        verbose_name_plural = "Notícias"