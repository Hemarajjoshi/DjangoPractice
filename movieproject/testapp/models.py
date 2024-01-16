from django.db import models

# Create your models here.
class Movies(models.Model):
    rdate = models.DateField()
    moviename = models.CharField(max_length = 100)
    hero = models.CharField(max_length = 100)
    heroine = models.CharField(max_length =100)
    rating = models.DecimalField(max_digits = 2 , decimal_places = 2)

