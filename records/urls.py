from django.urls import path
from .views import *
urlpatterns = [
    path('',index,name='index'),
    path('search',search,name='search'),
    path('delete/<str:pk>',delete ,name="delete")
]