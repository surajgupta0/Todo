# tasks/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from datetime import date

@login_required
def task_list(request):
    
    # Handle form submission for new task
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
    else:
        form = TaskForm()

    # Sorting parameters
    sort_by = request.GET.get('sort_by', 'created_at')  # Default sort by 'created_at'
    order = request.GET.get('order', 'desc')  # Default order is 'desc'
    
    # Determine order (ascending or descending)
    ordering = f'{"" if order == "asc" else "-"}{sort_by}'
    
    # Filter tasks for the logged-in user and apply sorting
    tasks = Task.objects.filter(user=request.user).order_by(ordering)
    
    # Calculate remaining days for each task
    today = date.today()
    for task in tasks:
        task.days_left = (task.due_date.date() - today).days if task.due_date else None

    # Render the template with tasks, form, and sorting info
    return render(request, 'task_list.html', {
        'tasks': tasks,
        'form': form,
        'sort_by': sort_by,
        'order': order
    })



@login_required
def task_edit(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'task_form.html', {'form': form})

@login_required
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == "POST":
        task.delete()
        return redirect('task_list')
    return render(request, 'task_confirm_delete.html', {'task': task})

@login_required
def task_complete(request, pk):
    sort_by = request.GET.get('sort_by', 'created_at')  # Default sorting by created_at
    order = request.GET.get('order', 'desc')  # Default order is descending
    task = get_object_or_404(Task, pk=pk, user=request.user)
    task.completed = not task.completed
    task.save()
    return redirect('/?sort_by='+sort_by+'&order='+order)
