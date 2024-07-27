from django.db import models

# Create your models here.
class students(models.Model):
    ID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)
    Contactno = models.BigIntegerField(null=True, blank=True, default=0)
    Email = models.EmailField(max_length=100, null=True, blank=True)
    password =  models.CharField(max_length=256, default='')
    def __str__(self) -> str:
        return self.Name