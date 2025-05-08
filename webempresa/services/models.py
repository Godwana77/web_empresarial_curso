from django.db import models

# Create your models here.
class Store(models.Model):
    title = models.CharField(max_length=100,verbose_name='Título')
    subtitle = models.CharField(max_length=100,verbose_name='Subtítulo')
    description = models.TextField(verbose_name='Descripción')
    image= models.ImageField(verbose_name='Imagen', upload_to='webempresa/images/')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')
    
    class Meta: # Configuración de la clase
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'
        ordering = ['-created_at']


    def __str__(self):
        return self.title