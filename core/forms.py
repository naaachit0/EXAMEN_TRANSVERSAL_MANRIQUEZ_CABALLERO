from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from .models import Cliente, Producto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ProductosForm(forms.ModelForm):

    class Meta:
        model = Producto
        fields = ['idProducto', 'nombreProducto', 'precioProducto', 'descripcionProducto',
        'imagen']
        labels = {
            'idProducto' : 'ID DEL PRODUCTO',
            'nombreProducto' : 'NOMBRE DEL PRODUCTO',
            'precioProducto' : 'PRECIO DEL PRODUCTO',
            'descripcionProducto' : 'DESCRIPCION DEL PRODUCTO',
            'imagen' : 'SELECCIONE IMAGEN DEL PRODUCTO'

        }

        widgets={

            'idProducto': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder' : 'Ingrese ID del producto',
                    'id' : 'idProducto'
                }
            ),

            'nombreProducto' : forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder' : 'Ingresa el nombre del producto',
                    'id' : 'nombreProducto' 
                }
            ),

            'precioProducto' : forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder' : 'Ingresa el precio del producto',
                    'id' : 'precioProducto'
                }
            ),

            'descripcionProducto' : forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder' : 'Ingresa descripcion del producto',
                    'id' : 'descripcionProducto'
                }
            )
        }


class ClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = ['rutCliente', 'nombreCliente', 'apellidoCliente', 'telefonoCliente', 'correoCliente', 'direccionCliente']
        labels = {
            'rutCliente' : 'RUT CLIENTE',
            'nombreCliente' : 'NOMBRE CLIENTE',
            'apellidoCliente' : 'APELLIDO CLIENTE',
            'telefonoCliente' : 'TELEFONO CLIENTE',
            'correoCliente' : 'CORREO CLIENTE',
            'direccionCliente' : 'DIRECCION CLIENTE',
        }

        widgets={
            'rutCliente' : forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder' : 'Ingresa RUT cliente',
                    'id' : 'rutCliente'
                }
            ),

            'nombreCliente' : forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder' : 'Ingresa nombre Cliente',
                    'id' : 'nombreCliente'
                }
            ),

            'apellidoCliente' : forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder' : 'Ingresa apellido Cliente',
                    'id' : 'apellidoCliente'
                }
            ),

            'telefonoCliente' : forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder' : 'Ingresa telefono Cliente',
                    'id' : 'telefonoCliente'
                }
            ),

            'correoCliente' : forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder' : 'Ingresa correo Cliente',
                    'id' : 'correoCliente'
                }
            ),

            'direccionCliente' : forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder' : 'Ingresa direccion Cliente',
                    'id' : 'direccionCliente'
                }
            )

        }


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', "first_name", "last_name", "email", "password1", "password2"]



