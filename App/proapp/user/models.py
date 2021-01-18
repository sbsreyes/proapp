#importing user model to create profile
from django.contrib.auth.models import User
#importing model instances
from django.db import models

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, verbose_name='Biografía')
    url = models.URLField(blank=True, null=True, verbose_name='Social')
    picture = models.ImageField(upload_to='user', verbose_name='Imagen de perfil')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualizacion')

    class Meta:
        verbose_name='Perfil'
        verbose_name_plural='Perfiles'

    def __str__(self):
        return self.bio
