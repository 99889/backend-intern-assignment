from django.urls import path
from tasks.views import create_task, retrieve_task, update_task, delete_task, list_tasks

urlpatterns = [
    path('tasks', create_task, name='create_task'),
    path('tasks/<int:task_id>', retrieve_task, name='retrieve_task'),
    path('tasks/<int:task_id>', update_task, name='update_task'),
    path('tasks/<int:task_id>', delete_task, name='delete_task'),
    path('tasks', list_tasks, name='list_tasks'),
]
