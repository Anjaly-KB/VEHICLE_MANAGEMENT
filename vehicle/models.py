from django.db import models

# Create your models here.


# my_choices=("2","3","4")


class Vehicles(models.Model):
    name=models.CharField(max_length=100)
    number=models.CharField(max_length=100)
    type=models.PositiveIntegerField()
    model=models.CharField(max_length=100)
    description=models.CharField(max_length=100)


    def __str__(self):
        return self.name