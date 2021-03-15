from django.db import models

class Enqiury(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.IntegerField(null=True)
    message = models.TextField(max_length= 1000)


#class Portfolio(models.Model):

