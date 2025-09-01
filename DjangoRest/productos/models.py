from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre=models.CharField(max_length=50)
    precio=models.DecimalField(max_digits=6,decimal_places=2)

    class Meta:
        verbose_name='Producto'
        verbose_name_plural='Productos'
    def __str__(self):
        return self.nombre    