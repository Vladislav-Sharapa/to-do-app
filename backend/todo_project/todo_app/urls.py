from . import views
from django.urls import path

urlpatterns = [
    path('', views.overview, name='test'),
    path('task_list/', views.task_list, name='task_list'),
    path('task_create/', views.CreateTask.as_view(), name='task_create'),
]
