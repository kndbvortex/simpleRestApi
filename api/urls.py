from django.urls import path
from api import views as viewApi

urlpatterns = [
    path('', viewApi.apiSimpleView, name='simple'),
    path('list/', viewApi.task_list, name="list_tasks"),
    path('detail/<str:id>', viewApi.task_detail, name="detail_tasks"),
    path('create/', viewApi.create_task, name='create-task'),
    path('update/<str:id>/', viewApi.update_task, name='update-task'),
    path('delete/<str:id>/', viewApi.delete_task, name='delete-task')
]