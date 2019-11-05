from django.urls import path
from . import views

app_name = 'movies'

urlpatterns=[
    path('', views.index, name="index"),
    path('create/', views.create, name='create'),
    path('load_data_csv/', views.load_data_csv, name='load_data_csv'),
    path('<int:movie_pk>', views.detail, name='detail'),
    path('<int:movie_pk>/update/', views.update, name='update'),
    path('<int:movie_pk>/delete/', views.delete, name="delete")
]