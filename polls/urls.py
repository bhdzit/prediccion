from django.urls import path
from . import views
from . import plots
urlpatterns = [
    path('', views.index, name='index'),
    path('buscar', views.buscar, name='buscar'),
    path('plots', plots.index, name='buscar'),
]