from django.db import models

class registrationModel(models.Model):
    fullname = models.CharField(max_length=50,null=False,blank=False)
    email = models.EmailField(unique=True,null=False,blank=False)
    password = models.CharField(max_length=20,null=False,blank=False)
    