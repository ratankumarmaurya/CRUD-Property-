from django.db import models
# Create your models here.

class Employee(models.Model):
    eid = models.CharField(max_length=20)
    ename = models.CharField(max_length=100)
    econtact = models.CharField(max_length=15)
    class Meta:
        db_table = "employee"

class WangUser(models.Model):
    username = models.CharField(max_length=32,unique=True)

    password = models.CharField(max_length=32)

    email = models.CharField(max_length=32)