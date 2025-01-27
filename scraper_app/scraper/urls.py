from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create-task/', views.create_task, name='create-task'),
    path('fetch-data/<int:task_id>/', views.fetch_data, name='fetch-data'),
]
