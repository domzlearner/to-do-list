from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete, UserLogin, UserLogout, UserRegister


urlpatterns = [
    path('login/', UserLogin.as_view(), name='login'),
    path('logout/', UserLogout.as_view(), name='logout'),
    path('register/', UserRegister.as_view(), name='register'),

    path('', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='details'),
    path('create-task/', TaskCreate.as_view(), name='create'),
    path('update-task/<int:pk>/', TaskUpdate.as_view(), name='update'),
    path('delete-task/<int:pk>/', TaskDelete.as_view(), name='delete'),
]