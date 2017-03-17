from django.db import models

class Bank(models.Model):
   # bank_name = models.CharField(max_length=200)
    pass

class Account(models.Model):
    bank_name = models.ForeignKey(Bank)
    ac_no = models.PositiveIntegerField()


class Customer(models.Model):
   # account_no = models.ForeignKey(Account)
    cust_id = models.PositiveIntegerField()
    cust_name = models.CharField(max_length=200)
    cust_address = models.TextField()
    cust_phone = models.CharField(max_length=10)
