from django.db import models

# Create your models here.
class Building (models.Model):
    name = models.CharField(max_length=30)
    photo = models.ImageField(null=True)

    def __str__(self):
        return self.name