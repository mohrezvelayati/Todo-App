from django.urls import path
from .views import TaskList, TaskCreate, TaskUpdate



urlpatterns = [
    path("", TaskList.as_view(), name='task_list'),
    path("create/", TaskCreate.as_view(), name='task_create'),
    path("update/<int:pk>/", TaskUpdate.as_view(), name='task_update'),
]

