from django.db import models

class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.CharField(max_length=20)
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
    class Meta:
        verbose_name_plural = "Proveedores"

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock_actual = models.IntegerField()
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

    def save(self, *args, **kwargs):
        if not self.proveedor.id and self.proveedor.nombre == "Agregar nuevo proveedor":
            proveedor_nuevo = Proveedor(nombre="Nuevo proveedor", apellido="", dni="", telefono="")
            proveedor_nuevo.save()
            self.proveedor = proveedor_nuevo
        super().save(*args, **kwargs)
