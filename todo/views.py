from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Task
from django.contrib.auth.decorators import login_required
from .forms import TaskForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm



@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)
    incomplete_task_count = tasks.filter(complete=False).count()

    search_input = request.GET.get('search-area') or ''
    if search_input:
        tasks = tasks.filter(title__icontains=search_input)  

    context = {
        'tasks': tasks,
        'count': incomplete_task_count,
        'search_input': search_input,
    }

    return render(request, 'todo/task_list.html', context)

@login_required
def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)

    context = {
        'task': task,
    }

    return render(request, 'todo/detail.html', context)

def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)  
            task.user = request.user        
            task.save()                    
            return redirect('tasks')        
    else:
        form = TaskForm()  

    return render(request, 'todo/tlogin.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome, {username}!")
                return redirect('tasks')  
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()

    return render(request, 'todo/login.html', {'form': form})

@login_required  
def logout_view(request):
    logout(request)  
    return redirect('login')

def register_view(request):
    if request.user.is_authenticated:
        return redirect('tasks')  

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f"Account created for {user.username}!")
            return redirect('tasks')
    else:
        form = UserCreationForm()
    
    return render(request, 'todo/register.html', {'form': form})

@login_required
def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)  
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()  
            return redirect('tasks')  
    else:
        form = TaskForm(instance=task)  

    return render(request, 'todo/task_form.html', {'form': form})


@login_required
def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)  

    if request.method == 'POST':
        task.delete()  
        return redirect('tasks')  

    return render(request, 'todo/task_confirm_delete.html', {'task': task})
