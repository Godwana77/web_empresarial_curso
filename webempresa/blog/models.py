from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre de la categoría')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        ordering = ['name']

    def __str__(self):
        return self.name
    
class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name='Título')
    content = models.TextField(verbose_name='Contenido')
    image = models.ImageField(upload_to='blog', verbose_name='Imagen', null=True, blank=True)
    published = models.DateTimeField(default=timezone.now(), verbose_name='Publicado')
    author= models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Autor')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')
    category = models.ManyToManyField(Category, verbose_name='Categoría')# on_delete=models.CASCADE,

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['-created_at']

    def __str__(self):
        return self.title