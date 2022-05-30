
from turtle import update
from unicodedata import name
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.addandshow,name='addandshow'),
    path('message/',views.message,name='message'),
    path('delete/<int:id>',views.delete_data,name='deletedata'),
    path('<int:id>',views.update_data,name='updatedata'),
]
