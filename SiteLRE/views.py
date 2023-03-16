from django.shortcuts import render

from Pesquisador.models import Pesquisador
from Projeto.models import Projeto
from Artigo.models import Artigo

def home(request):
    lista_professores = Pesquisador.objects.filter(tipo='1', ativo=True)
    lista_pesquisadores = Pesquisador.objects.filter(ativo=True)
    lista_projetos = Projeto.objects.all()
    lista_artigos = Artigo.objects.all()

    informacoes = {
        'lista_professores': lista_professores,
        'lista_pesquisadores': lista_pesquisadores,
        'lista_projetos': lista_projetos,
        'lista_artigos': lista_artigos
    }

    return render(request, 'index.html', informacoes)