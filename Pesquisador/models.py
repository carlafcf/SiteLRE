from django.db import models

TIPO_PESQUISADOR = [
    ('1', 'Professor'),
    ('2', 'Pesquisador'),
    ('3', 'Aluno de pós-graduação'),
    ('4', 'Aluno de IC'),
    ('5', 'Estagiário'),
    ('6', 'Outro'),
]

GENERO = [
    ('1', 'Feminino'),
    ('2', 'Masculino'),
    ('3', 'Outro'),
]

TITULACAO = [
    ('1', 'Doutorado completo'),
    ('2', 'Mestrado completo'),
    ('3', 'Graduação completa'),
    ('4', 'Graduação em andamento'),
]

# Create your models here.
class Pesquisador (models.Model):
    tipo = models.CharField(max_length=2, choices=TIPO_PESQUISADOR, null=False, blank=False, verbose_name="Tipo de pesquisador")

    nome = models.CharField(max_length=200, null=False, blank=False, verbose_name="Nome")
    email = models.EmailField(null=False, blank=False, verbose_name="E-mail")
    contato = models.CharField(max_length=20, null=False, blank=False, verbose_name="Contato")

    genero = models.CharField(max_length=1, choices=GENERO, null=False, blank=False, verbose_name="Gênero")
    titulacao = models.CharField(max_length=1, choices=TITULACAO, null=False, blank=False, verbose_name="Contato")

    instituicao = models.CharField(max_length=50, null=False, blank=False, verbose_name="Instituição")
    departamento = models.CharField(max_length=50, null=False, blank=False, verbose_name="Departamento")
    curso = models.CharField(max_length=50, null=False, blank=False, verbose_name="Curso")

    area_pesquisa = models.CharField(max_length=200, verbose_name="Área de pesquisa")
    descricao_pesquisador = models.TextField(verbose_name="Descrição do pesquisador")

    ativo = models.BooleanField(default=True, null=False, blank=False, verbose_name="Ativo")
    # foto

    def __str__(self) -> str:
        return self.nome

    # class Meta:
        # ordering