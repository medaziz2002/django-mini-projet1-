from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('info/',views.info ,name='info'),
    path('stage/',views.stage ,name='stage'),
    path('formation/',views.formation, name='formation'),
    path('competance/',views.competance, name='competance'),
]