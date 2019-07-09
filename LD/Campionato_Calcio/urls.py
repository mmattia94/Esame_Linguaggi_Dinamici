from django.urls import path
from . import views


app_name = 'Campionato_Calcio'
urlpatterns = [
    path('calendario/', views.sel_calendario, name='sel_calendario'),
    path('calendario/<int:camp_id>/', views.calendario, name='calendario'),
    path('classifica/', views.sel_calendario, name='sel_calendario'),
    path('classifica/<int:camp_id>/', views.classifica, name='classifica'),
    path('risultati/', views.sel_giornata, name='sel_giornata'),
    path('risultati/<int:camp_id>/<int:giornata_id>/<str:ar>', views.risultati, name="giornata"),
    path('schedina/', views.sel_giornata, name='sel_giornata'),
    path('schedina/<int:camp_id>/<int:giornata_id>/<str:ar>', views.schedina, name="schedina"),
    path('squadra/', views.sel_squadra, name='sel_squadra'),
    path('squadra/<int:camp_id>/<str:nome_squadra>', views.squadra, name='squadra'),
]