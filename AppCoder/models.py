from django.db import models

## CLASE 24
from django.contrib.auth.models import User

class Avatar(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.FileField(upload_to="media/avatares", null=True, blank=True)

    def __str__(self):
        return f"{self.user} - {self.imagen}"


class Marca(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    categoria = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.marca} {self.modelo} {self.color}"


class Auto(models.Model):
    marca = models.CharField(max_length=30)
    modelo = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.marca} ({self.modelo})"


############### pseudo0-instagram #############################


class Perfil(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=2200)

    def __str__(self):
        return f"{self.usuario}"


class Post(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.FileField(upload_to="media/posts", null=True, blank=True)
    epigrafe = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.epigrafe}"


class Comentario(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    texto = models.CharField(max_length=2200)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f"@{self.autor}: '{self.post}'"