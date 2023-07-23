from django.contrib import admin
from django.urls import path, include
from app import views
urlpatterns = [
    path('', views.insert, name='insert'),
      path('show/', views.show, name='show' ),
    path('delete/<int:category_id>/', views.delete, name="delete"),
    path('edit/<int:category_id>/', views.edit, name="edit"),
    path('update/<int:category_id>', views.updated, name='update')
]
