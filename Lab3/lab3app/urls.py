from django.urls import path
from . import views

app_name = 'lab3app'

urlpatterns = [
    path('', views.home, name='home'),
    path('comparison/', views.comparison, name='comparison'),
    path('activate-engines/', views.activate_engines, name='activate_engines'),
    path('dtl-filters/', views.dtl_filters, name='dtl_filters'),
]
