from . import views
from django.urls import path

urlpatterns = [
    path('', views.overview, name='test'),
    path('task_list/', views.task_list, name='task_list')
]
