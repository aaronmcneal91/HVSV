from django.db import models

class Citizen(models.Model):
    name = models.CharField(max_length=255)
    alter_ego = models.CharField(max_length=255)
    power = models.CharField(max_length=255)
    affiliation = models.CharField(max_length=10)
  

def __str__(self):
    return f"{self.name}"
