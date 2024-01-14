from django.db import models
from datetime import date
import PIL.Image

from Pesquisador.models import Pesquisador

class AreaPesquisa (models.Model):
    nome = models.CharField(max_length=300, null=False, blank=False, verbose_name="Nome")
    status = models.BooleanField(default=True, verbose_name="Status")
    foto = models.ImageField(upload_to ='areas_pesquisa/fotos/', default='pesquisadores/fotos/default.png') 

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = PIL.Image.open(self.foto)
        width, height = img.size
        target_width = 400
        h_coefficient = width/400
        target_height = height/h_coefficient
        img = img.resize((int(target_width), int(target_height)), PIL.Image.Resampling.LANCZOS)
        img.save(self.foto.path, quality=100)
        img.close()
        self.foto.close()

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Área de pesquisa"
        verbose_name_plural = "Áreas de pesquisa"

class Projeto (models.Model):
    titulo = models.CharField(max_length=1000, null=False, blank=False, verbose_name="Título")
    descricao = models.TextField(null=False, blank=False, verbose_name="Descrição")
    data_inicio = models.DateField(default=date.today, null=False, blank=False, verbose_name="Data de início")
    data_fim = models.DateField(default=date.today, verbose_name="Data de fim")

    participantes = models.ManyToManyField(Pesquisador, through='Participacao')
    areas_pesquisa = models.ManyToManyField(AreaPesquisa, through="AreasPesquisaProjeto")

    foto = models.ImageField(upload_to ='projetos/fotos/', null=-True, blank=True, default='pesquisadores/fotos/default.png') 

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = PIL.Image.open(self.foto)
        width, height = img.size
        target_width = 400
        h_coefficient = width/400
        target_height = height/h_coefficient
        img = img.resize((int(target_width), int(target_height)), PIL.Image.Resampling.LANCZOS)
        img.save(self.foto.path, quality=100)
        img.close()
        self.foto.close()

    # imagem

    def __str__(self) -> str:
        return self.titulo

    class Meta:
        verbose_name = "Projeto"
        verbose_name_plural = "Projetos"

class Participacao(models.Model):
    pesquisador = models.ForeignKey(Pesquisador, on_delete=models.RESTRICT)
    projeto = models.ForeignKey(Projeto, on_delete=models.RESTRICT)
    data_entrada = models.DateField(default=date.today, verbose_name='Data de entrada')
    ativo = models.BooleanField(default=True, null=False, blank=False, verbose_name="Ativo")

    class Meta:
        verbose_name = "Participação em projeto"
        verbose_name_plural = "Participações em projetos"

class AreasPesquisaProjeto(models.Model):
    area_pesquisa = models.ForeignKey(AreaPesquisa, on_delete=models.RESTRICT)
    projeto = models.ForeignKey(Projeto, on_delete=models.RESTRICT)

    class Meta:
        verbose_name = "Área de pesquisa de projeto"
        verbose_name_plural = "Áreas de pesquisa de projetos"
