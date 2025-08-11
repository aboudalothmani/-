from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='books_index'),
    path('show/', views.show, name='books_show'),
    path('edit/<int:id>/', views.edit, name='books_edit'),
    path('delete/<int:id>/', views.delete, name='books_delete'),
]
