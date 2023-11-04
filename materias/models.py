from django.db import models
from django.conf import settings
from datetime import datetime


class materia(models.Model):
    name = models.CharField(max_length=255)
    professor = models.CharField(max_length=255)
    date = models.DateField()
    imagem = models.URLField(max_length=200, null=True)
    descricao = models.TextField()

    def __str__(self):
        return f'{self.name}'


class Review(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    likes = models.IntegerField(default=0)
    date = models.DateTimeField(default=datetime.now())
    materia = models.ForeignKey(materia, on_delete=models.CASCADE)

    def __str__(self):
        return f'"{self.text}" - {self.author.username}'
# Create your models here.
