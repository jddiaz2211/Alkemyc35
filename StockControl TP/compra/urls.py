from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('listar-productos/', views.listar_productos, name='listar_productos'),
    path('listar-proveedores/', views.listar_proveedores, name='listar_proveedores'),
    path('agregar-producto/', views.agregar_producto, name='agregar_producto'),
    path('agregar-proveedor/', views.agregar_proveedor, name='agregar_proveedor'),
    path('succes/', views.succes, name='succes'),
]