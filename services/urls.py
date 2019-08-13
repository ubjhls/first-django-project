from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('artii/', views.artii),
    path('artii_result/', views.artii_result),
    path('workshop/', views.workshop),
    path('workshop_result/', views.workshop_result)
]