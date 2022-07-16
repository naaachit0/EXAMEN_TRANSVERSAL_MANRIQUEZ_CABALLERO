from django.urls import path 
from .views import lista_cliente

urlpatterns=[ 
    path('lista_cliente', lista_cliente, name="lista_cliente"),
]