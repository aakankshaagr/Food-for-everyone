from django.db import models
from django.http import HttpResponse
from django.contrib import messages

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=122)
    phone=models.IntegerField()
    email = models.EmailField(max_length=122)
    subject = models.CharField(max_length=300)
    message = models.CharField(max_length=700)
    entrydate=models.DateField()
    date=models.DateTimeField(auto_now_add=True,null=True)
    
    def __str__(self):
        return self.name
    
