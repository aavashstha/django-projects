from django.urls import path
from .views import (
    TaskCreateView,
    TaskDetailView,
    TaskListView,
    TaskDeleteView,
    TaskUpdateView
)

app_name = 'tasks'
urlpatterns = [
    path('', TaskListView.as_view(), name='tasks-list'),
    path('create/', TaskCreateView.as_view(), name='tasks-create'),
    path('<int:id>/', TaskDetailView.as_view(), name='tasks-detail'),
    path('<int:id>/delete/', TaskDeleteView.as_view(), name='tasks-delete'),
    path('<int:id>/update/', TaskUpdateView.as_view(), name='tasks-update'),
]

