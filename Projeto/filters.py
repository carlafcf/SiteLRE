import django_filters
from Projeto.models import Projeto

class ProjetoFiltro(django_filters.FilterSet):
    titulo = django_filters.CharFilter(lookup_expr='icontains')
    descricao = django_filters.CharFilter(lookup_expr='icontains')
    participantes = django_filters.CharFilter(field_name='participantes__nome', lookup_expr='icontains')
    areas_pesquisa = django_filters.CharFilter(field_name='areas_pesquisa__nome', lookup_expr='icontains')

    class Meta:
        model = Projeto
        fields = {'titulo', 'descricao', 'participantes__nome', 'areas_pesquisa__nome'}