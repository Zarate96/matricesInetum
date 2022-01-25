from django.urls import path
from . import views
from .views import HomePageView,CategoriaListView,CategoriaDetail, TablaDetail



app_name= 'core'
urlpatterns = [
	path('', HomePageView.as_view(), name="home"),
	path('categorias/', CategoriaListView.as_view(), name="categoria_list"),
	path('<int:pk>/', CategoriaDetail.as_view(), name="categoria_detail"),
	path('tabla/<int:pk>/', TablaDetail.as_view(), name="tabla_detail"),

]