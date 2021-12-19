from django.db import models
from django.db.models.fields import related
from django.core.validators import MaxValueValidator, MinValueValidator


class Car(models.Model):
    make = models.CharField(max_length=60)
    model = models.CharField(max_length=60)
    def __str__(self):
        return f"{self.make} {self.model}"


class Rating(models.Model):
	car_id = models.ForeignKey(Car, related_name="ratings", on_delete=models.CASCADE)
	rate = models.FloatField(validators = [MinValueValidator(0.0), MaxValueValidator(5.0)])

