from django.http import HttpRequest
from django.shortcuts import render

from Models.Parcial.forms import FormularioProducto, FormularioMarca, FormularioCategoria
from Models.Parcial.models import Producto, Categoria, Marca


class FormularioProductoView(HttpRequest):

    def registraProducto(request):
        producto = FormularioProducto()
        return render(request, "ProductoIndex.html", {"form": producto})

    def procesar_producto(request):
        producto = FormularioProducto(request.POST)
        if producto.is_valid():
            producto.save()
            producto = FormularioProducto()

        return render(request, "ProductoIndex.html", {"form": producto, "mensaje": 'OK'})

    def listar_productos(request):
        producto = Producto.objects.all()
        return render(request, "ListarProducto.html", {"producto": producto})

    def edit_producto(request, id_producto):
        producto = Producto.objects.filter(id=id_producto).first()
        form = FormularioProducto(isinstance=producto)
        return render(request, "ProductoEdit.html", {"form":form, "producto": producto})

    def actualizar_producto(request, id_producto):
        producto = Producto.objects.get(pk=id_producto)
        form = FormularioProducto(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            producto = Producto.objects.all()
            return render(request, "ListarProducto.html", {"producto": producto})

    def delete_producto(request, id_producto):
        producto = Producto.objects.get(pk=id_producto)
        producto.delete()
        producto = Producto.objects.all()
        return render(request, "ListarProducto.html", {"producto": producto, "mensaje": 'OK'})


class FormularioMarcaView(HttpRequest):

    def registraMarca(request):
        marca = FormularioMarca()
        return render(request, "MarcaIndex.html", {"form": marca})

    def procesar_marca(request):
        marca = FormularioMarca(request.POST)
        if marca.is_valid():
            marca.save()
            marca = FormularioMarca()

        return render(request, "MarcaIndex.html", {"form": marca, "mensaje": 'OK'})

    def listar_marcas(request):
        marca = Marca.objects.all()
        return render(request, "ListarMarca.html", {"marca": marca})

    def edit_marca(request, id_marca):
        marca = Marca.objects.filter(id=id_marca).first()
        form = FormularioMarca(isinstance=marca)
        return render(request, "MarcaEdit.html", {"form":form, "marca": marca})

    def actualizar_marca(request, id_marca):
        marca = Marca.objects.get(pk=id_marca)
        form = FormularioMarca(request.POST, instance=marca)
        if form.is_valid():
            form.save()
            marca = Marca.objects.all()
            return render(request, "ListarMarca.html", {"marca": marca})

    def delete_marca(request, id_marca):
        marca = Marca.objects.get(pk=id_marca)
        marca.delete()
        marca = Marca.objects.all()
        return render(request, "ListarMarca.html", {"marca": marca, "mensaje": 'OK'})


class FormularioCategoriaView(HttpRequest):

    def registraCategoria(request):
        categoria = FormularioCategoria()
        return render(request, "CategoriaIndex.html", {"form": categoria})


    def procesar_categoria(request):
        categoria = FormularioCategoria(request.POST)
        if categoria.is_valid():
            categoria.save()
            categoria = FormularioCategoria

        return render(request, "CategoriaIndex.html", {"form": categoria, "mensaje": 'OK'})

    def listar_categorias(request):
        categorias = Categoria.objects.all()
        return  render(request, "ListarCategoria.html", {"categoria": categorias})

    def edit_categoria(request, id_categoria):
        categoria = Categoria.objects.filter(id=id_categoria).first()
        form = FormularioCategoria(isinstance=categoria)
        return render(request, "CategoriaEdit.html", {"form":form, "categoria": categoria})

    def actualizar_categoria(request, id_categoria):
        categoria = Categoria.objects.get(pk=id_categoria)
        form = FormularioCategoria(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            categoria = Categoria.objects.all()
            return render(request, "ListarCategoria.html", {"categoria": categoria})

    def delete_categoria(request, id_categoria):
        categoria = Categoria.objects.get(pk=id_categoria)
        categoria.delete()
        categoria = Categoria.objects.all()
        return render(request, "ListarCategoria.html", {"categoria": categoria, "mensaje": 'OK'})


