from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *
from django.views.generic.list import ListView, MultipleObjectMixin
from django.views.generic.detail import DetailView
# Create your views here.


# Vista para la pagina Home y ordenar productos en la portada
class HomePageView(TemplateView):
    template_name = "core/base.html"


class CategoriaListView(ListView):
    template_name = "core/index.html"
    model = Categoria


class CategoriaDetail(DetailView, MultipleObjectMixin):
    template_name = "core/empresa.html"
    model = Categoria

    def get_context_data(self, **kwargs):
        object_list = Empresa.objects.filter(categoria_id=self.object.id)
        context = super(CategoriaDetail, self).get_context_data(object_list=object_list, **kwargs)
        return context



class TablaDetail(DetailView):
    template_name = "core/tabla.html"
    model = Empresa

    def get_context_data(self, **kwargs):
        object_list = TablaEscalacion.objects.filter(empresa_id=self.object.id)
        context = super(TablaDetail, self).get_context_data(object_list=object_list, **kwargs)
        return context