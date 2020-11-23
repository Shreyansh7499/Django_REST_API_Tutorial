from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# class Person(models.Model):
#     first_name = models.CharField(max_length = 30)
#     last_name = models.CharField(max_length = 30)

class Person(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    age = models.IntegerField(default = 18, validators = [MaxValueValidator(100), MinValueValidator(1)])