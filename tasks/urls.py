from django.urls import path
from.views import TaskAPIView, TaskDetailAPIView
urlpatterns = [
    path('task/', TaskAPIView.as_view(), name='tasks'),
    path('task/<int:pk>', TaskDetailAPIView.as_view(), name= 'task-detail')
]