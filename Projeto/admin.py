from django.contrib import admin
from Projeto.models import Projeto, Participacao, AreaPesquisa, AreasPesquisaProjeto

# Register your models here.
admin.site.register(Projeto)
admin.site.register(Participacao)
admin.site.register(AreaPesquisa)
admin.site.register(AreasPesquisaProjeto)