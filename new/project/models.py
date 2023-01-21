from django.db import models

# Create your models here.
class Employee(models.Model):
    Name = models.CharField(max_length=200)
    Email = models.EmailField(unique=True)
    Address = models.CharField(max_length=100)
    Phone = models.IntegerField()

    def __str__(self):
        return self.Name

    

