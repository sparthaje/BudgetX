from django.shortcuts import render
from dashboard.models import    BudgetCategory, SubBudgets
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect

def index(request):
    return render(request, 'upload/index.html')

def budgethandler(request):
    category= request.POST["category"]
    user = request.user
    amount=request.POST["amount"]
    cat = user.budgetcategory_set.create(name=category, total_cost=amount)
    cat.save()
    context = {"name" : category}
    return render(request, 'upload/subcategory.html', context)

def sub_handler(request):
    category = request.POST["category"]
    sub = request.POST["name"]
    percent = request.POST["percent"]
    bcatagory = BudgetCategory.objects.get(name__iexact = category)
    bcatagory.subbudgets_set.create(name = sub, percent = percent)
    
    context = {"name" : bcatagory.name}
    
    return render(request, 'upload/subcategory.html', context)
