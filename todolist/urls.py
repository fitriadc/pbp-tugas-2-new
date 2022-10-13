from django.urls import path
from todolist.views import create_todo_ajax, delete_task, register, login_user, show_todolist, logout_user, create_todo, delete_task, update_task_status, show_todolist_json


app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name="show_todolist"),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-todo/', create_todo, name="create_todo"),
    path('delete/<int:id>', delete_task, name="delete_task"),
    path('update/<int:id>', update_task_status, name="update_task_status"),
    path('json/', show_todolist_json, name="show_todolist_json"),
    path('add/', create_todo_ajax, name="create_todo_ajax"),
]
