from django.db import models

# Create your models here.


class users(models.Model):

    name = models.CharField(max_length=45)
    username = models.CharField(max_length=45)
    password = models.CharField(max_length=45)