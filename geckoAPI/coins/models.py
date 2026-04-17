from django.db import models

class Question(models.Model):
    coin = models.CharField(max_length=3)
    price = models.FloatField(default=0)
    date = models.DateTimeField()