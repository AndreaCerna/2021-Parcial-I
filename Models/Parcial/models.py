from django.db import models


class Categoria(models.Model):
    nombre = models.CharField(max_length=100, null=False, unique=True)
    def __str__(self):
        return self.nombre

class Marca(models.Model):
    marca = models.CharField(max_length=100, null=False, unique=True)
    def __str__(self):
        return self.marca

class Producto(models.Model):
    nombre = models.ForeignKey(Categoria, null=False, on_delete=models.CASCADE)
    marca = models.ForeignKey(Marca, null=False, on_delete=models.CASCADE)
    nombre_producto = models.CharField(max_length=200, unique=True, null=False)
    descripcion_producto = models.TextField(null=True)
    def __str__(self):
        return self.nombre_producto


