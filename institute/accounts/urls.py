from django.urls import path
from . import views

urlpatterns = [
    path('', views.account_login, name='login'),
    path('logout/', views.account_logout, name='logout'),
]