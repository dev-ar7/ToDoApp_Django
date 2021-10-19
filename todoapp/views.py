from django import forms
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse, response
from django.template import RequestContext
from .models import Username, Task
from .forms import UsernameForm, TaskForm

# Create your views here.


def check_user_validity(request):
    # Check If The User Exist In Database Or Not
    try:
        return Username.objects.get(username_exact=request.COOKIES['username'])
    except Exception:
        return False


def tasks(request):
    if request.method == 'POST':
        form = TaskForm(request.POST or None)
        if form.is_valid():
            user = Username.objects.get(
                username=request.COOKIES.get('username'))
            temp = form.save(commit=False)
            temp.username = user
            temp.save()
            form = TaskForm()
        tasks = Task.objects.filter(
            username=request.COOKIES.get('username')).order_by('priority')
        context = {
            'form': form,
            'tasks': tasks,
            'user': user
        }
        return render(request, 'tasks.html', context)
    else:
        if 'username' not in request.COOKIES:
            from django.utils.crypto import get_random_string
            unique_id = get_random_string(length=50)
            username = Username()
            username.username = unique_id
            username.save()
            response = render(request, 'todoapp/tasks.html', {})
            response.set_cookie('username', username,
                                max_age=604800)  # 604800 = 1 Week
            return response
        form = TaskForm()
        tasks = Task.objects.filter(
            username=request.COOKIES.get('username')).order_by('priority')
        user = Username.objects.filter(
            username=request.COOKIES.get('username'))
    return render(request, 'tasks.html', {'form': form, 'tasks': tasks, 'user': user})


def delete(request, id):
    if 'username' in request.COOKIES and check_user_validity(request):
        # check The User Trying To Access The Task Is Actully Created By Himself
        Task.objects.filter(id=id, username=Username.objects.get(
            username__exact=request.COOKIES['userrname'])).delete()
        return redirect(reverse('tasks'))
    else:
        return HttpResponse("You Are Not Allowed To Access This Resource!")


def complete(request, id):
    if 'username' in request.COOKIES and check_user_validity(request):
        try:
            task = Task.objects.get(id=id, username=Username.objects.get(
                username__exact=request.COOKIES['username']))
            if task.complete:
                task.complete = 0
            else:
                task.complete = 1
            task.save()
            return redirect('/')
        except Exception:
            return HttpResponse("Sorry You Are Not Allowed To Access This Task")
    else:
        return HttpResponse("You Are Not Allowed To Access This Resources ")


def clear(request):
    Username.objects.filter(username=request.COOKIES['username']).delete()
    response = HttpResponseRedirect('/tasks/')
    response.delete_cookie('username')
    return response
