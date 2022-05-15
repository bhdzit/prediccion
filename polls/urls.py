from django.urls import path
from . import views
from . import plots
from . import prediccion
from . import prediccion_lineal
urlpatterns = [
    path('', views.index, name='index'),
    path('buscar', views.buscar, name='buscar'),
    path('plots', plots.index, name='buscar'),
    path('ggplot',prediccion.ggplot, name='ggplot'),
    path('linial',prediccion_lineal.prediccionLinial, name='linial')
]