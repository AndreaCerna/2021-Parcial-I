"""PrimerParcialAndrea URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path

from Models.Parcial.views import FormularioProductoView, FormularioMarcaView, FormularioCategoriaView
from Views.HomeView import HomeView
urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', HomeView.home, name='home'),
    path('guardarProducto/', FormularioProductoView.registraProducto, name="guardarProducto"),
    path('mostrarProducto/', FormularioProductoView.procesar_producto, name="mostrarProducto"),
    path('listarProducto/', FormularioProductoView.listar_productos, name="listarProducto"),
    path('editarProducto/<int:id_producto>', FormularioProductoView.edit_producto, name="editarproducto"),
    path('actualizarProducto/<int:id_producto>', FormularioProductoView.actualizar_producto, name="actualizarproducto"),
    path('eliminarProducto/<int:id_producto>', FormularioProductoView.delete_producto, name="eliminarproducto"),

    path('guardarMarca/', FormularioMarcaView.registraMarca, name="guardarMarca"),
    path('mostrarMarca/', FormularioMarcaView.procesar_marca, name="mostrarMarca"),
    path('listarMarca/', FormularioMarcaView.listar_marcas, name="listarMarca"),
    path('editarMarca/<int:id_marca>', FormularioMarcaView.edit_marca, name="editarmarca"),
    path('actualizarMarca/<int:id_marca>', FormularioMarcaView.actualizar_marca, name="actualizarmarca"),
    path('eliminarMarca/<int:id_marca>', FormularioMarcaView.delete_marca, name="eliminarmarca"),

    path('guardarCategoria/', FormularioCategoriaView.registraCategoria, name="guardarCategoria"),
    path('mostrarCategoria/', FormularioCategoriaView.procesar_categoria, name="mostrarCategoria"),
    path('listarCategoria/', FormularioCategoriaView.listar_categorias, name="listarCategoria"),
    path('editarCategoria/<int:id_categoria>', FormularioCategoriaView.edit_categoria, name="editarcategoria"),
    path('actualizarCategoria/<int:id_categoria>', FormularioCategoriaView.actualizar_categoria, name="actualizarcategoria"),
    path('eliminarCategoria/<int:id_categoria>', FormularioCategoriaView.delete_categoria, name="eliminarcategoria"),


]
