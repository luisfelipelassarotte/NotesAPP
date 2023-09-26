from django.db import models

# Create your models here.

class Note(models.Model):
    titulo=models.CharField(max_length=255)
    conteudo=models.TextField()
    date_created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
     return self.titulo  