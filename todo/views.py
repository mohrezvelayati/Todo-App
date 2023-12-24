from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import View
from django.urls import reverse_lazy
from .forms import TaskUpdateForm

# Create your views here.

from .models import Task

class TaskList(ListView):
    model = Task
    context_object_name = 'task'
    template_name = "todo/task_list.html"
    
    # def get_queryset(self):
    #     return self.model.objects.filter(user=self.request.user)
    

class TaskCreate(CreateView):
    model = Task
    fields = ['title']
    success_url = reverse_lazy("task_list")

    def form_valid(self, form):
        form.instance.user = self.request.user    
        return super(TaskCreate,self).form_valid(form)



class TaskUpdate(UpdateView):
    model = Task
    success_url = reverse_lazy("task_list")
    form_class = TaskUpdateForm
    template_name = "todo/task_update.html"



class TaskComplete(View):
    model = Task
    success_url = reverse_lazy("task_list")
    
    
    def get(self, request, *args, **kwargs):
        object = Task.objects.get(id=kwargs.get('pk'))
        object.complete = True
        object.save()
        return redirect(self.success_url)
    


class TaskDelete(DeleteView):
    model = Task
    success_url = reverse_lazy("task_list")
    # context_object_name = "task"  ''' i dont know usage '''
    

    # def get(self, request, *args, **kwargs):
    #     return self.post(request, *args, **kwargs)

    # def get_queryset(self):
    #     return self.model.objects.filter(user=self.request.user)