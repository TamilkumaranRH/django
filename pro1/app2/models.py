from django.db import models
from.models import*
# Create your models here.
class details(models.Model):
    name=models.CharField(max_length=100)
    contactno = models.BigIntegerField(null=True, blank=True, default=0)
    email = models.EmailField(max_length=100, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    password =  models.CharField(max_length=256, default='')
    def __str__(self):
        return self.name
