from django.db import models
from django.utils import timezone
# Create your models here.



JOB_TYPE = (
    ('Full Time', 'Full Time'),
    ('Part Time', 'Part Time'),
)

class Bloger(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    title = models.CharField(max_length=80)
    job_type = models.CharField(max_length=20, choices=JOB_TYPE)    
    description = models.TextField(blank=True,null = True)
    # created = models.DateTimeField(default=timezone.now())
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.firstName
