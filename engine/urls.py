from django.urls import path
from engine import views


urlpatterns = [
     path('', views.index, name='home'),
     path('add/', views.add, name='add'),
     path('edit/<int:id>/', views.edit, name='edit'),
     path('delete/<int:id>/', views.delete, name='delete')
]