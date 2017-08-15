from django.db import models

# Create your models here.
# model Item
class Item(models.Model):
    item_name = models.CharField(max_length=50)
    item_description = models.CharField(max_length=50)
    item_cost = models.FloatField()
