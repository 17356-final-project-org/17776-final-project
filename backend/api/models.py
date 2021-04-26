from django.db import models

class Item(models.Model):
    name = models.CharField(max_length = 50)
    nominal_price = models.FloatField()
    lowest_price = models.FloatField()
    item_url = models.CharField(max_length=500)

    def __str__(self):
        return self.name
