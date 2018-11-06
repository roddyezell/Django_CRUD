from django.urls import path, include
from CRUD_app import views

app_name = 'CRUD_app'

urlpatterns = [
    path('newuser/', views.newuser, name='newuser'),
    path('show/', views.showusers, name='showusers'),
    ]