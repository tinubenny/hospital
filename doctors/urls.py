from django.urls import path
from . import views

urlpatterns=[
    path('home',views.doctors_home,name='home'),
]