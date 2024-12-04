from django.urls import path
from . import views


urlpatterns = [
    path('', views.language_list, name='language_list'),
    path('add/', views.add_language, name='add_language'),

       ]