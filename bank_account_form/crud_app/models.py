
from django.db import models

class Account(models.Model):

    TYPE = [('SAV','Saving'),('CUR','Current'),('FIX','Fixed'),('DEM','Demat'),('RECU','Recurring')]
    cust_name = models.CharField(max_length=20)
    account_no = models.IntegerField()
    account_type = models.CharField(max_length=10, choices=TYPE)
    bank_name = models.CharField(max_length=20)
    branch_name = models.CharField(max_length=20)
    branch_code = models.IntegerField()
    address = models.CharField(max_length=20)
    dob = models.DateField()