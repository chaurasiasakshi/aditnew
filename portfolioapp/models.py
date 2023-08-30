from django.db import models

# Create your models here.
class promodel(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.CharField(max_length=255)
    
    
    