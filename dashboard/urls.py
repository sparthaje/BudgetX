from django.urls import path
from . import views

app_name = 'login'
urlpatterns = [
    path('', views.dash, name='dash'),
    path('detail/', views.redirect, name='redirect'),
]