from django.db import models

# Create your models here.

class Curso(models.Model):
    codigo=models.CharField(primary_key=True, max_length=10)
    nombre=models.CharField(max_length=50)
    creditos=models.PositiveSmallIntegerField()
   
    
    def __str__(self):
        texto = '{0} ({1})'
        return texto.format(self.nombre, self.creditos)
    
class Boton(models.Model):
    nombre=models.CharField(max_length=50)
    creditos=models.PositiveSmallIntegerField()
    
    def __str__(self):
        texto = '{0} ({1})'
        return texto.format(self.nombre, self.creditos)
        
class Turno(models.Model):
    nombre = models.CharField(max_length=100)
    fecha = models.DateField()
    hora = models.TimeField()
  
    
    def __str__(self):
        texto = '{0} {1} {2}'
        return texto.format(self.nombre, self.fecha, self.hora)