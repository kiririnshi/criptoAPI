from django.db import models

class Moneda(models.Model): # CLP
    nombre = models.CharField(max_length=10, unique=True)

class Activo(models.Model): # BTC
    nombre = models.CharField(max_length=10, unique=True)

class Precio(models.Model): # CLP vs BTC
    moneda = models.ForeignKey(Moneda, on_delete=models.CASCADE)
    activo = models.ForeignKey(Activo, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=20, decimal_places=8) # Es mala practica usar float para datos financieros??? 
    fecha_precio = models.DateTimeField() # La fecha en donde se reporto este precio.

    class Meta:
        unique_together = ('moneda', 'activo', 'fecha_precio')

        