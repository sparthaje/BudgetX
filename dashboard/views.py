from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import BudgetCategory, SubBudgets

# Create your views here.
def dash(request):
    context = {
        "budgets": request.user.budgetcategory_set.all()
    }
    return render(request, 'dashboard/dash.html', context)

def redirect(request):
    bname = request.POST["budget_name"]
    bcategory = BudgetCategory.objects.get(name__startswith = bname)
    sbudgets = bcategory.subbudgets_set.all()
    context = {
        "bcategory": bcategory,
        "sbudgets": sbudgets,
    }
    return render(request, 'dashboard/pi.html', context)