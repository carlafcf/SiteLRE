from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views import generic

import json

from SiteLRE.forms import ContatoForm
from Pesquisador.models import Pesquisador
from Projeto.models import Projeto, AreaPesquisa
from Artigo.models import Artigo
from Artigo.filters import ArtigoFiltro
from Projeto.filters import ProjetoFiltro

def home(request):
    lista_professores = Pesquisador.objects.filter(tipo='1', ativo=True)
    lista_pesquisadores = Pesquisador.objects.filter(ativo=True)
    lista_projetos = Projeto.objects.all().order_by('-data_fim')[:6]
    lista_artigos = Artigo.objects.all()
    lista_areas_pesquisa = AreaPesquisa.objects.filter(status=True)
    form = ContatoForm()

    informacoes = {
        'lista_professores': lista_professores,
        'lista_pesquisadores': lista_pesquisadores,
        'lista_projetos': lista_projetos,
        'lista_artigos': lista_artigos,
        'lista_areas_pesquisa': lista_areas_pesquisa,
        'form': form
    }

    return render(request, 'index.html', informacoes)

def contato(request):
    form = ContatoForm(request.POST)
    if form.is_valid():
        form.send_email()
        retorno = "Mensagem enviada com sucesso!"
        form = ContatoForm()
    else:
        retorno = "Não foi possível enviar a mensagem."
        
    return HttpResponse(
        json.dumps(retorno),
        content_type="application/json"
    )

class ListarProjetos(generic.ListView):
    model = Projeto
    paginate_by = 5
    template_name = 'projetos.html'
    context_object_name = 'lista_projetos'

def listar_projetos(request):
    lista_projetos = Projeto.objects.all().order_by("titulo")

    page = request.GET.get('page', 1)

    paginator = Paginator(lista_projetos, 5)
    try:
        page_object = paginator.page(page)
    except PageNotAnInteger:
        page_object = paginator.page(1)
    except EmptyPage:
        page_object = paginator.page(paginator.num_pages)

    areas_pesquisa = AreaPesquisa.objects.filter(status=True).order_by('nome')

    informacoes = {
        'lista_projetos': page_object,
        'areas_pesquisa': areas_pesquisa,
    }

    return render(request, 'projetos.html', informacoes)

class ListarProjetosFiltrados(generic.ListView):
    model = Projeto
    template_name = 'projetos.html'
    context_object_name = 'lista_projetos'
    paginate_by = 2

    def get_queryset(self):
        # qs = super().get_queryset()
        # print(self.request.GET.get('areas_pesquisa'))
        projetos_filtrados = ProjetoFiltro(self.request.GET, queryset=Projeto.objects.all().order_by("-data_fim"))
        qs_filtrada = projetos_filtrados.qs
        return qs_filtrada

    def get_context_data(self,**kwargs):
        context = super(ListarProjetosFiltrados,self).get_context_data(**kwargs)
        # projeto_filtrado = ProjetoFiltro(self.request.GET, queryset=Projeto.objects.all().order_by("-data_fim"))
        context['lista_areas_pesquisa'] = AreaPesquisa.objects.all().order_by('nome')
        # context['projeto_filtrado'] = projeto_filtrado.qs
        # context['form_filtro'] = projeto_filtrado.form
        print(self.request.GET.get('areas_pesquisa'))
        context['titulo'] = self.request.GET.get('titulo') if self.request.GET.get('titulo') is not '' else None
        context['descricao'] = self.request.GET.get('descricao') if self.request.GET.get('descricao') is not '' else None
        context['participantes'] = self.request.GET.get('participantes') if self.request.GET.get('participantes') is not '' else None
        context['areas_pesquisa'] = self.request.GET.get('areas_pesquisa') if self.request.GET.get('areas_pesquisa') is not '' else None
        return context

class ListarArtigosFiltrados(generic.ListView):
    model = Artigo
    template_name = 'artigos.html'
    context_object_name = 'lista_artigos'
    paginate_by = 2

    def get_queryset(self):
        # qs = super().get_queryset()
        artigos_filtrados = ArtigoFiltro(self.request.GET, queryset=Artigo.objects.all().order_by("-ano"))
        qs_filtrada = artigos_filtrados.qs
        return qs_filtrada

    def get_context_data(self,**kwargs):
        context = super(ListarArtigosFiltrados,self).get_context_data(**kwargs)
        # artigo_filtrado = ArtigoFiltro(self.request.GET, queryset=Artigo.objects.all().order_by("-ano"))
        # context['artigo_filtrado'] = artigo_filtrado.qs
        # context['form_filtro'] = artigo_filtrado.form
        context['titulo'] = self.request.GET.get('titulo') if self.request.GET.get('titulo') is not '' else None
        context['publicacao'] = self.request.GET.get('publicacao') if self.request.GET.get('publicacao') is not '' else None
        context['ano'] = int(self.request.GET.get('ano')) if self.request.GET.get('ano') is not '' and self.request.GET.get('ano') is not None else 0
        context['resumo'] = self.request.GET.get('resumo') if self.request.GET.get('resumo') is not '' else None
        context['palavras_chave'] = self.request.GET.get('palavras_chave') if self.request.GET.get('palavras_chave') is not '' else None
        context['autores'] = self.request.GET.get('autores') if self.request.GET.get('autores') is not '' else None
        return context
    
class InformacoesProjeto(generic.DetailView):
    model = Projeto
    template_name = 'projeto_informacoes.html'
    context_object_name = 'projeto'

def listar_artigos(request):
    lista_artigos = Artigo.objects.all().order_by("-ano")

    page = request.GET.get('page', 1)

    paginator = Paginator(lista_artigos, 2)
    try:
        page_object = paginator.page(page)
    except PageNotAnInteger:
        page_object = paginator.page(1)
    except EmptyPage:
        page_object = paginator.page(paginator.num_pages)

    informacoes = {
        'lista_artigos': page_object,
    }

    return render(request, 'artigos.html', informacoes)