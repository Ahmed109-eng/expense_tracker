from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='tasks'),
    path('task/<int:pk>/', views.task_detail, name='detail'),  
    path('create-task/', views.task_create, name='task-create'),
    path('login/', views.login_view, name='login'), 
    path('logout/', views.logout_view, name='logout'), 
    path('register/', views.register_view, name='register'), 
    path('task/<int:pk>/update/', views.task_update, name='task-update'), 
    path('task/<int:pk>/delete/', views.delete_task, name='task-delete'),
]