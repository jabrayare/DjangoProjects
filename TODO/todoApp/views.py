from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import task
from .forms import taskForm


def index(request):
    tasks = task.objects.all()
    form = taskForm()
    if request.method == 'POST':
        form = taskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    context = {
        'tasks': tasks,
        'form': form,
    }
    return render(request, 'todoApp/index.html', context)


def update_task(request, pk):
    tasks = task.objects.get(id=pk)
    form = taskForm(instance=tasks)
    if request.method == 'POST':
        form = taskForm(request.POST, instance=tasks)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {
        'form': form,
    }
    return render(request, 'todoApp/update_tasks.html', context)


def deleteTasks(request, pk):
    user = request.user
    print(user)
    print(user.is_authenticated)
    item = task.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('/')
    context = {
        'item': item,
    }
    return render(request, 'todoApp/delete.html', context)
