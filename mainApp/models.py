from django.db import models

class Cafe(models.Model):
    name = models.CharField(max_length=15)
    latitude= models.FloatField(default=0.0)
    longtitude = models.FloatField(default=0.0)