from django.urls import path
from . import views

app_name = 'login'
urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name = 'signup'),
    path('login_handler/', views.login_handler, name='login_handler'),
    path('signup_handler/', views.signup_handler, name = 'signup_handler'),

]