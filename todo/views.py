from django.shortcuts import render, redirect, reverse
from . models import Todo


def todo_list(request):
    if request.method =='POST':
        description = request.POST['description']

        if description:
            Todo.objects.create(description=description)
            return redirect('todo_list')
        
    context = Todo.objects.filter(is_done=False)

    return render(request, 'todo/todo_list.html', {'object_list': context})


def todo_detail(request, pk):
    todo = Todo.objects.get(pk=pk)


    if request.method == 'POST':
        todo.is_done = True
        todo.save()

        return redirect('todo_list')
    
    return render(request, 'todo/todo_detail.html', {'object_list': todo})


def todo_delete(request, pk):
    if request.method == 'DELETE':
        todo = Todo.objects.get(pk=pk)
        todo.delete()
        return redirect('todo_list')
    
    # return render(request, 'todo/todo_delete.html', {'todo': todo})

