from django.db import models

# Create your models here.


class Configuracion(models.Model):
    id_configuracion = models.AutoField(db_column='id', primary_key=True) 
    dato = models.CharField(max_length=100)
    valor = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 

    def _str_(self):
        return self.nombre.dato
    
