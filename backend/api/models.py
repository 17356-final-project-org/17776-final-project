from django.db import models

class Merchant(models.Model):
    name = models.CharField(max_length = 50)

class Item(models.Model):
    name = models.CharField(max_length = 50)
    category = models.CharField(max_length = 100)
    merchant = models.ForeignKey(Merchant, on_delete = models.CASCADE)
