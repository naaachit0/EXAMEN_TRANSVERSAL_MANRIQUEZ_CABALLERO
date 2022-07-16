from django.urls import path 
from .views import index, catalogo, contacto, quienesSomos, formulario, minijuegogatos, agregar_producto, listar_productos,\
 modificar_producto, eliminar_producto, agregar_cliente, listar_cliente, modificar_cliente, eliminar_cliente, registro, carrito


urlpatterns=[
    path('', index, name="index"),
    path('catalogo/', catalogo, name="catalogo"),
    path('contacto/', contacto, name="contacto"),
    path('quienesSomos/', quienesSomos, name="quienesSomos"),
    path('formulario/', formulario, name="formulario"),
    path('minijuegogatos/', minijuegogatos, name="minijuegogatos"),
    path('agregar_producto/', agregar_producto, name="agregar_producto"),
    path('listar_productos/', listar_productos, name="listar_productos"),
    path('modificar_producto/<id>/', modificar_producto, name="modificar_producto"),
    path('eliminar_producto/<id>/', eliminar_producto, name="eliminar_producto"),
    path('agregar_cliente/', agregar_cliente, name="agregar_cliente"),
    path('listar_cliente/', listar_cliente, name="listar_cliente"),
    path('modificar_cliente/<id>', modificar_cliente, name='modificar_cliente'),
    path('eliminar_cliente/<id>', eliminar_cliente, name='eliminar_cliente'),
    path('registro/', registro, name="registro"),
    path('carrito/', carrito, name="carrito"),
]