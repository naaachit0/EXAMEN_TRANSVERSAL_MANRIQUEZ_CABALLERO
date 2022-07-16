from django.db import models

# Create your models here.

class Producto(models.Model):
    idProducto = models.IntegerField(primary_key=True, verbose_name ='ID PRODUCTO')
    nombreProducto = models.CharField(max_length=50, verbose_name= 'NOMBRE PRODUCTO')
    precioProducto = models.IntegerField(verbose_name = 'PRECIO PRODUCTO')
    descripcionProducto = models.TextField(max_length = 50, verbose_name='DESCRIPCION DEL PRODUCTO' )
    imagen = models.ImageField(upload_to="productos", null=True)

    def __str__(self):
        return self.nombreProducto

class Cliente(models.Model):
    rutCliente = models.CharField(max_length=9, primary_key=True, verbose_name='RUT' )
    nombreCliente = models.CharField(max_length=20, verbose_name='NOMBRE CLIENTE' )
    apellidoCliente = models.CharField(max_length=20, verbose_name='APELLIDO CLIENTE' )
    telefonoCliente = models.IntegerField(verbose_name='TELEFONO CLIENTE')
    correoCliente = models.CharField(max_length=50, verbose_name='CORREO CLIENTE', default='CORREO')
    direccionCliente = models.CharField(max_length=50, verbose_name='DIRECCION CLIENTE', default='DIRECCION')

    def __str__(self):
        return self.rutCliente