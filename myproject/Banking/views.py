from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.contrib.auth.models import User 

class Bank():
    #    return render("Hello ... ! Its Bank Page")
    def display(request):
        t = Account.objects.all()
        print("**** BANK ****", t)
        return render(request, 'Banking/home.html')

class Account(Bank):
    pass

class Employee(Bank):
    pass

class Customer(Account): 
    def menu(request):
        return render(request, 'Banking/customer_home_page.html')

    def create(request):
        return render(request, 'Banking/createcustomer.html')
    
