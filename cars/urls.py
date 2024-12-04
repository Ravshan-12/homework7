from django.urls import path
from . import views
urlpatterns = [
    path('', views.car_list, name='car_list'),
    path('add/', views.add_car, name='add_car'),

            ]