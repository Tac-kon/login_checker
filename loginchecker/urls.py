from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('whole/', views.whole, name='whole'),
    path('create/', views.create, name='create'),
    path('delete/<int:pk>', views.delete, name='delete'),
]