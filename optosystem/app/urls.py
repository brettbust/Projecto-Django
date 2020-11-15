from django.urls import path

#importando vistas
from app import views


urlpatterns = [
    path('',views.inicio, name ="Inicio"),
    path('secretaria',views.secretaria, name ="Secretaria"),
    path('profesional_Medico',views.profesional_Medico, name ="Profesional_Médico"),
    path('ventas',views.ventas, name ="Ventas"),
    path('taller',views.taller, name ="Taller"),
    path('gerencia',views.gerencia, name ="Gerencia"),
]