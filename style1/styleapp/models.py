from django.db import models

# Create your models here.
class Student(models.Model):  
    first_name = models.CharField(max_length=30)  
    last_name = models.CharField(max_length=30)  
    email_id = models.EmailField()  
    enter_password = models.CharField(max_length=256, default='')  
    confirm_password =  models.CharField(max_length=256, default='')
    
    def __str__(self):  
        return "%s %s" % (self.first_name, self.last_name)  