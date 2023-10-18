from django.db import models
from django.utils import timezone

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    phone = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    desc = models.TextField()
    date = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return self.name
    
