from django.db import models

# Create your models here.

class productos(models.Model):
   nombre_del_producto = models.CharField(max_length= 20, verbose_name='nombre del producto')
   precio_del_producto = models.FloatField(max_length= 20, verbose_name= 'precio del producto')
   subtotal = models.FloatField(max_length= 20, verbose_name= 'subtotal')

def __str__(self):
    return self.nombre_del_producto, self.precio_del_prodcuto, self.subtotal

   
class pedidos(models.Model):
    estado_del_pedido = models.CharField(max_length= 20, verbose_name= 'estado del pedido')
    tipo_de_pago = models.CharField(max_length= 20, verbose_name= 'tipo de pago')

    
def __str__(self):
    return self.estado_del_pedido, self.tipo_de_pago


class paciente(models.Model):
  nombre: models.CharField(max_length= 20, verbose_name= 'nombre del paciente')
  apellido: models.CharField(max_length= 20, verbose_name= 'apellido del paciente')
  edad: models.IntegerField(max_length= 3, verbose_name= 'edad del paciente')
  peso: models.FloatField(max_length= 3, verbose_name= 'peso')
  altura: models.FloatField(max_length= 3, verbose_name= 'altura')

def __str__(self):
    return self.nombre, self.apellido, self.edad, self.peso, self.altura
   
class turno(models.Model):
    fecha_de_turno = models.DateField(verbose_name= 'fecha de turno')
    medico_asignado =  models.CharField(max_length= 20, verbose_name= 'medico asignado')

def __str__(self):
    return self.fecha_de_turno, self.medico_asignado
class historial(models.Model):
    historial_medico = models.CharField(max_length= 200, verbose_name= 'historial medico')
    
    def __str__(self):
       return self.historial_medico
