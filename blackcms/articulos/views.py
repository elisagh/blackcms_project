from django.shortcuts import render, redirect
from articulos.models import Articulo, Categoria
from articulos.forms import ArticuloForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def inicio(request):
	articulos = Articulo.objects.all()
	categorias = Categoria.objects.all()
	return render(request, 'articulos/inicio.html', {'articulos' : articulos, 'categorias' : categorias})


def ver_articulo(request, id_articulo):
	articulo = Articulo.objects.get(pk=id_articulo)
	categorias = Categoria.objects.all()
	return render(request, 'articulos/ver_articulo.html', {'articulo' : articulo, 'categorias' : categorias})


def view_category(request, slug_categoria):
	categoria = Categoria.objects.get(slug=slug_categoria)
	articulos = Articulo.objects.filter(categoria=categoria)
	return render(request, 'articulos/view_category.html', {'articulos' : articulos, 'categoria' : categoria})


def buscar(request):
	busqueda = request.GET["busqueda"]
	articulos = Articulo.objects.filter(titulo__icontains=busqueda)
	return render(request, 'articulos/buscar.html', {'articulos' : articulos})


@login_required
def publicar(request):
	if request.method == 'POST': 
		formulario = ArticuloForm(request.POST,request.FILES)
		if formulario.is_valid():
			nuevoarticulo = formulario.save(commit=False)
			nuevoarticulo.autor = request.user
			nuevoarticulo.save()
			messages.success(request, 'Se han introducido tus datos.')
			return redirect("inicio")
	else:
		formulario = ArticuloForm()
	return render(request, 'articulos/publicar.html', {'formulario' : formulario})
