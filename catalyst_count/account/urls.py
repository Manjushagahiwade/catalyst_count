
from django.contrib import admin
from django.urls import path
from .views import UserListView,UserDeleteView,UserCreateView


urlpatterns = [
    path('create_user/', UserCreateView.as_view(), name='user-create'),
    path('user_list/', UserListView.as_view(), name='user-list'),
    path('delete-user/<int:pk>/', UserDeleteView.as_view(), name='delete-user')

]
