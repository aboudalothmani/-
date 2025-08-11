from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='tasks_index'),
    path('show/', views.show, name='tasks_show'),
    path('edit/<int:id>/', views.edit, name='tasks_edit'),
    path('delete/<int:id>/', views.delete, name='tasks_delete'),
]
