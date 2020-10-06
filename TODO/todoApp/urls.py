from django.urls import path
from . import views

urlpatterns = [
    path('update_task/<str:pk>/', views.update_task, name='update_task'),
    path('', views.index, name='index'),
    path('delete/<str:pk>/', views.deleteTasks, name='delete'),

]
