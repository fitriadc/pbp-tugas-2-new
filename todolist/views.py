from re import T
from django.core import serializers
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from todolist.models import Task
import datetime
from django.http import HttpRequest, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.


@login_required(login_url='/todolist/login/')
def show_todolist(request):
    username = request.user.username
    todo = Task.objects.filter(user=request.user)
    context = {
        'data_todolist': todo,
        'username': username,
    }
    return render(request, "todolist.html", context)


def create_todo(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        new_todo = Task(user=request.user, title=title,
                        description=description)
        new_todo.save()
        return redirect('todolist:show_todolist')
    return render(request, "create_todo.html")


def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')

    context = {'form': form}
    return render(request, 'register.html', context)


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(
                reverse("todolist:show_todolist"))  # membuat response
            # membuat cookie last_login dan menambahkannya ke dalam response
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)


def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response


def update_task_status(request, id):
    task = Task.objects.get(pk=id)
    if task.is_finished:
        task.is_finished = False
    else:
        task.is_finished = True
    task.save()
    return redirect('todolist:show_todolist')


def delete_task(request, id):
    task = Task.objects.get(pk=id)
    task.delete()
    return redirect('todolist:show_todolist')


@login_required(login_url="/todolist/login")
def show_todolist_json(request):
    todo = Task.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', todo), content_type='application/json')


def create_todo_ajax(request):
    if request.method == "POST":
        new_todo = Task(
            title=request.POST.get('title'),
            description=request.POST.get("description"),
            user=request.user,
        )
        new_todo.save()
        return HttpResponse(b"Task Created!", status=201)
    return HttpResponse("Invalid method", status_code=405)
