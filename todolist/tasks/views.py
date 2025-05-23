from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .forms import TaskModelForm, TaskUpdateModelForm
from .models import Task

from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
) 


# Create your views here.

class TaskObjectMixin(object):
    model = Task
    
    def get_object(self):
        my_id = self.kwargs.get('id')
        obj = None
        if my_id is not None:
            obj = get_object_or_404(self.model, id=my_id)
        return obj



class TaskCreateView(CreateView):
    template_name = 'tasks/task_create.html'
    form_class = TaskModelForm

    def form_valid(self, form):
        return super().form_valid(form)
    

class TaskDetailView(TaskObjectMixin, DetailView):
    template_name = 'tasks/task_detail.html'
    
    

class TaskListView(ListView):
    template_name = 'tasks/task_list.html'
    queryset = Task.objects.all()

    
class TaskDeleteView(TaskObjectMixin, DeleteView):
    template_name = 'tasks/task_delete.html'
    
    def get_success_url(self):
        return reverse('tasks:tasks-list')
    

class TaskUpdateView(TaskObjectMixin, UpdateView):
    template_name = 'tasks/task_update.html'
    form_class = TaskUpdateModelForm