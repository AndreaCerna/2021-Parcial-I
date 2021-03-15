from django import forms

from Models.Parcial.models import Producto, Marca, Categoria


class FormularioProducto(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'

class FormularioMarca(forms.ModelForm):
    class Meta:
        model = Marca
        fields = '__all__'

class FormularioCategoria(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'