from django.shortcuts import render
from dashboard.models import    BudgetCategory, SubBudgets
from django.contrib.auth.models import User
<<<<<<< HEAD
from django.http import HttpResponse, HttpResponseRedirect
=======
from django.http import HttpResponse
>>>>>>> 8b2838949d5bb6f6ae0a5750450c821e0f68be28

def index(request):
    return render(request, 'upload/index.html')

def budgethandler(request):
    category= request.POST["category"]
    user = request.user
    amount=request.POST["amount"]
    cat = user.budgetcategory_set.create(name=category, total_cost=amount)
    cat.save()
<<<<<<< HEAD
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
=======
    return render(request, 'upload/subcategory.html', {'category' : category})
>>>>>>> 8b2838949d5bb6f6ae0a5750450c821e0f68be28
