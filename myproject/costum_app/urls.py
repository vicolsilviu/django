from django.urls import path
from costum_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
]

