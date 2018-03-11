from django.shortcuts import render
from dashboard.models import BudgetReader, SubBudgets
from django.contrib.auth.models import User
def index(request):
    return render(request, 'upload/index.html')
def budgethandler(request):
    category= request.POST["category"]
    u=request.user()
    amount=request.POST["amount"]
    cat=user.BudgetReader.create(user=u, name=category, total_cost=amount)
    cat.save()
    return HttpResponseRedirect("/subcategory/")
def subcategory(request):
    return render(request, 'upload/subcategory')
