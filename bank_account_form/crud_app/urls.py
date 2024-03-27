from django.urls import path
from .views import create_account,show_account,update_account,delete_account

urlpatterns = [
    path('create/',create_account,name='create_url'),
    path('show/',show_account,name='show_url'),
    path('update/<int:pk>/',update_account,name='update_url'),
    path('delete/<int:pk>/',delete_account,name='delete_url')
]