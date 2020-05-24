
from django.urls import path
from . import views

from .views import ChartData, get_data, home

urlpatterns = [
    path('', views.home, name='home'),
    path('api/data',views.get_data,name='get-data'),
    path('api/chart/data',views.ChartData.as_view(),name='chart-data'),
]
