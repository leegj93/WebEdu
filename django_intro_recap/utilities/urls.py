from django.urls import path
from . import views

urlpatterns=[
    path('', views.index),
    path('artii/', views.artii),
    path('out_artii/', views.out_artii),
]