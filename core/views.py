from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProductosForm, ClienteForm, CustomUserCreationForm
from .models import Producto, Cliente
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required
# Create your views here.
def index(request):
    return render (request, 'index.html')

def catalogo(request):
    return render(request, 'catalogo.html')

def contacto(request):
    return render(request, 'contacto.html')

def quienesSomos(request):
    return render(request, 'quienesSomos.html')

def formulario(request):
    return render(request, 'formulario.html')

def minijuegogatos(request):
    return render(request, 'minijuegogatos.html')

def carrito(request):
    return render(request, 'carrito.html')

@permission_required('core.add_producto')
def agregar_producto(request):
    data = {
        'form': ProductosForm()
    }

    if request.method == 'POST':
        formulario = ProductosForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
        else:
            data["form"] = formulario

    return render(request, 'agregar.html', data)


@permission_required('core.view_producto')
def listar_productos(request):
    productos = Producto.objects.all()

    data={
        'productos': productos
    }


    return render(request, 'listar.html', data)

@permission_required('core.change_producto')
def modificar_producto(request, id):
    producto = Producto.objects.get(idProducto=id)
    data ={
        'form': ProductosForm (instance = producto)
    }
    if request.method=='POST':
        formulario = ProductosForm(data=request.POST, instance = producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to='listar_productos')
    return render(request, 'modificar.html', data)

@permission_required('core.delete_producto')
def eliminar_producto(request, id):
    producto = Producto.objects.get(idProducto=id)
    producto.delete()
    return redirect(to="listar_productos")

@permission_required('core.add_cliente')
def agregar_cliente(request):
    data = {
        'form' : ClienteForm()

    }
    if request.method == 'POST':
        formulario = ClienteForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
        else:
            data["form"] = formulario

    return render(request, 'agregarcliente.html', data)

@permission_required('core.view_cliente')
def listar_cliente(request):
    clientes = Cliente.objects.all()
    data={
        'clientes' : clientes
    }
    return render(request, 'listarclientes.html', data)

@permission_required('core.change_cliente')
def modificar_cliente(request, id):
    clientes = Cliente.objects.get(rutCliente=id)
    data={
        'form' : ClienteForm(instance = clientes)
    }
    if request.method=='POST':
        formulario = ClienteForm(data=request.POST, instance = clientes)
        if formulario.is_valid():
            formulario.save()
        return redirect(to='listar_cliente')
    return render(request,'modificarcliente.html', data)
@permission_required('core.delete_cliente')
def eliminar_cliente(request, id):
    clientes = Cliente.objects.get(rutCliente=id)
    clientes.delete()
    return redirect(to='listar_cliente')

def registro(request):
    data ={
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            return redirect(to="index")
        data["form"] = formulario 
    return render(request, 'registration/registro.html', data) 