from django.urls import path
from .views import birthday_list, add_birthday, edit_birthday

urlpatterns = [
    path('', birthday_list, name='birthday_list'),
    path('add/', add_birthday, name='add_birthday'),
    path('edit/<int:pk>/', edit_birthday, name='edit_birthday'),
]