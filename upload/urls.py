from django.urls import path
from . import views

app_name = 'upload'
urlpatterns = [
    path('', views.index, name='index'),
    path('budgethandler/', views.budgethandler, name = 'budgethandler'),
    path('sub_handler/', views.sub_handler, name = 'sub_handler'),
]