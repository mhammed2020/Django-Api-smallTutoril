from django.db import models
from django.utils import timezone
# Create your models here.


class Bloger(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=50)
    description = models.TextField(blank=True,null = True)
    created = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.firstName

 

