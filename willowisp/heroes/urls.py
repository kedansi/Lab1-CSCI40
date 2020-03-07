from django.contrib import admin
from django.urls import path

from . import views


urlpatterns = [
    path('', views.HeroesView.as_view(), name='heroes_view'),
    path('heroes/', views.HeroesView.as_view(), name='heroes_view'),
    path('hero/cloud/', views.CloudView.as_view(), name='cloud_view'),
    path('hero/sunflowey/', views.SunfloweyView.as_view(), name='sunflowey_view'),
    path('hero/jester/', views.JesterView.as_view(), name='jester_view'),

]
