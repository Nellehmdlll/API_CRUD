from django.urls import path
from .views import TaskCreateView,TaskRetrieveUpdateDeleteView

urlpatterns = [
    path('tasks/', TaskCreateView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskRetrieveUpdateDeleteView.as_view(), name='task-retrieve-update-delete'),

    # path('create_task',TaskCreateView,'create_task'),
    # path('update_task',TaskRetrieveUpdateDeleteView,'update_task')

]
