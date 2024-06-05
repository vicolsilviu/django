# from django.urls import path
# from costum_app import views

# urlpatterns = [
#     path('', views.index, name='index'),
#     path('index/', views.index, name='index'),
# ]
# from django.urls import path
# from . import views

# urlpatterns = [
#     path('index/', views.index, name='index'),
# ]

# costum_app/urls.py
from django.urls import path
from .views import index

urlpatterns = [
    path('index/', index, name='index'),
]
