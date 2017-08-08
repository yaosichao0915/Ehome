from django.shortcuts import get_object_or_404,render
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Statement
@login_required(login_url='/admin')
def index(request):
      
    return render(request, 'Book/index.html')

def show(request):
    a = Statement.objects.order_by('-issued_date')[:]
    return render(request, 'Book/show.html', {'statement':a})

def insert(request):
    
    if request.method == 'POST':
        date = request.POST['date']
        balance = request.POST['balance']
        summary = request.POST['summary']
        category = request.POST['category']
        balance_type = request.POST['balance_type']
        updb = Statement(issued_date=date,balance=balance,category=category,summary=summary,balance_type=balance_type)
        updb.save()
        return HttpResponseRedirect('/book/show/')
        
def modify(request):
    req = get_object_or_404(Statement, pk=request.POST['id'])
    return render(request, 'Book/modify.html',{'req':req})
    
def complete_change(request):
    req = get_object_or_404(Statement, pk=request.POST['id'])
    req.issued_date = request.POST['date']
    req.balance = request.POST['balance']
    req.summary = request.POST['summary']
    req.category = request.POST['category']
    req.balance_type = request.POST['balance_type']
    req.save()
    return HttpResponseRedirect('/book/show/')

def delete(request):
    req = get_object_or_404(Statement, pk=request.POST['id'])
    req.delete()
    return HttpResponseRedirect('/book/show/')