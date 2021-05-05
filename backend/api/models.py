from django.db import models
from django.contrib.auth.models import User

class Item(models.Model):
    seller = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    nominal_price = models.FloatField()
    lowest_price = models.FloatField()
    item_url = models.CharField(max_length=500)

    def __str__(self):
        return self.name
