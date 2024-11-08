# tasks/urls.py
from django.urls import path
from .views import task_list, task_edit, task_delete, task_complete

urlpatterns = [
    path('', task_list, name='task_list'),
    path('<int:pk>/edit/', task_edit, name='task_edit'),
    path('<int:pk>/delete/', task_delete, name='task_delete'),
    path('<int:pk>/complete/', task_complete, name='task_complete'),
]
