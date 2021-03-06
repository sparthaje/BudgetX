from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import BudgetCategory, SubBudgets
from random import randint

# Create your views here.
def dash(request):
    context = {
        "budgets": request.user.budgetcategory_set.all()
    }
    return render(request, 'dashboard/dash.html', context)

def redirect(request):
    bname = request.POST["budget_name"]
    bcategory = BudgetCategory.objects.get(name__startswith = bname)
    colors = []
    sbudgets = bcategory.subbudgets_set.all()
    
    for i in range(len(sbudgets)):
        r, g, b = randint(0,255), randint(0, 255), randint(0, 255)
        s = "rgb({0}, {1}, {2})".format(r, g, b)
        print(s)
        colors.append(s)
    
    print(colors)
    context = {
        "bcategory": bcategory,
        "sbudgets": [(sbudgets[s], colors[s]) for s in range(len(sbudgets))],
        "r": len(sbudgets),
    }
    print(context['sbudgets'])
    return render(request, 'dashboard/pi.html', context)