from django.shortcuts import render, redirect
from .models import Customer

# Create your views here.
from django.http import HttpResponse

def index(request):
    return render(request, "bank/index.html")

def transaction(request):
    customer = Customer.objects.all
    return render(request, "bank/transaction.html", {'customer' : customer})

def register(request):
    if request.method == 'POST':
            name = request.POST['name']
            email = request.POST['email']
            bankno = request.POST['bankno']
            balance = request.POST['balance']
            customer = Customer()
            customer.bankno = bankno
            customer.name =  name
            customer.email = email
            
            customer.balance = balance        
            customer.save()
            return redirect("/")
    else:    
        return render(request, "bank/transaction.html")
def customers(request):
    customer = Customer.objects.all()
    return render(request, "bank/customers.html", {'customer':customer})

def transfer(request):     
        if request.method=='POST' and 'send' in request.POST:
            bankno = request.POST['bankno']
            bal = request.POST['balance']
            customer = Customer.objects.get(bankno = bankno)
            customer.balance = customer.balance + int(bal)
            customer.save()
            return render(request, "bank/transfer.html")
    
        elif request.method=='POST' and 'draw' in request.POST:
            bankno = request.POST['bankno']
            bal = request.POST['balance']
            customer = Customer.objects.get(bankno = bankno)
            customer.balance = customer.balance - int(bal)
            customer.save()
            return render(request, "bank/transfer.html")

        else: 
            return render(request, "bank/transfer.html")

    
