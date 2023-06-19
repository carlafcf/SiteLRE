import django_filters
from Artigo.models import Artigo

class ArtigoFiltro(django_filters.FilterSet):
    titulo = django_filters.CharFilter(lookup_expr='icontains')
    ano = django_filters.CharFilter(lookup_expr='icontains')
    publicacao = django_filters.CharFilter(lookup_expr='icontains')
    palavras_chave = django_filters.CharFilter(lookup_expr='icontains')
    resumo = django_filters.CharFilter(lookup_expr='icontains')
    autores = django_filters.CharFilter(field_name='autores__nome', lookup_expr='icontains')

    class Meta:
        model = Artigo
        fields = {'autores'}