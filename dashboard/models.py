from django.db import models
from django.contrib.auth.models import User

class BudgetReader(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length = 50)
    total_cost = models.IntegerField(default = 0)

class SubBudgets(models.Model):
    budget_catagory = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length = 50)
    percent = models.IntegerField(default = 0)
    