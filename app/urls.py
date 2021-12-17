from django.urls import path
from . import views	
                    
urlpatterns = [
    path('', views.index),
    path('camion/add', views.addCamion),
    path('ruta/add', views.addRuta),
    path('prueba', views.prueba),
]
