from django.db import models

# Create your models here.

class film(models.Model):
    nume = models.TextField(default=None)
    descriere = models.TextField(default=None)
    score = models.TextField(default=None)
    regizor = models.TextField(default=None)
    star = models.TextField(default=None)
    storyline = models.TextField(default=None)
    data = models.DateField(default=None)
    durata = models.DurationField(default=None)
    azi = models.BooleanField(default=False)
    imagine = models.ImageField(upload_to='static/images')
    id_gen = models.ForeignKey('gen', on_delete=models.CASCADE)
    ora1 = models.TimeField(default=None)
    ora2 = models.TimeField(default=None)
    trailer_link = models.TextField(default=None)

class gen(models.Model):
    nume = models.TextField()