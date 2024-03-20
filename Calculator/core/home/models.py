from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
# class Numbers(models.Model):
#     numbers = models.CharField(max_lenght=100)
