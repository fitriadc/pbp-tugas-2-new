from django.urls import path
from todolist.views import register, login_user, show_todolist, logout_user, create_todo


app_name = 'todolist'

urlpatterns = [
    # sesuaikan dengan nama fungsi yang dibuat
    path('', show_todolist, name="show_todolist"),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-todo/', create_todo, name="create_todo"),
]
