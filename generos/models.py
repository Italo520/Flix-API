from django.db import models


class Genero(models.Model):
    nome = models.CharField(max_length=200)


    def __str__(self):
        return self.nome
