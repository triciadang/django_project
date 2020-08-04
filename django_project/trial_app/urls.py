from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='app-home'),
    path('list_of_books/',views.home,name='list'),
    path('hello_world/', views.subpage, name='app-subpage'),
    path('adding_books/', views.addBooks, name='add-books'),
]

