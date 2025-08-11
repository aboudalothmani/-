from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='notes_index'),
    path('show/', views.show, name='notes_show'),
    path('edit/<int:id>/', views.edit, name='notes_edit'),
    path('delete/<int:id>/', views.delete, name='notes_delete'),
]
