from django.db import models

# Create your models here.
class Building (models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return   f"{self.name} is the building name"

