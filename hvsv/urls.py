from django.urls import path
from .import views

urlpatterns= [
    path('', views.citizen_list),
]