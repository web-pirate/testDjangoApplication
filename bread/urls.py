from django.urls import path
from bread import views

urlpatterns = [
    path('', views.home, name="home"),
    path('add/', views.add, name='add'),
    path('register/', views.register, name='register'),
    path('update/', views.update, name='update'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]
