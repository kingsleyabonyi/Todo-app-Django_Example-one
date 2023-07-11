from django.shortcuts import render, redirect
from . forms import Taskform
from . models import Task


def index(request):
    form = Taskform()

    if request.method == 'POST':
        form = Taskform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        
    tasks = Task.objects.all()

    return render(request, 'task/index.html', {'task_form': form, 'tasks': tasks})


def update_task(request, pk):
    task = Task.objects.get(pk=pk)
    form = Taskform(instance=task)
    if request.method == 'POST':
        form = Taskform(request.POST, instance=pk)
        if form.is_valid():
            form.save()
            return redirect('index')

   

    return render(request, 'task/update_task.html', {'task_edit_form': form})


def delete_task(request,pk):
    task = Task.objects.get(pk=pk)
    if request.method == 'DELETE':
        task.delete()
        return redirect('index')