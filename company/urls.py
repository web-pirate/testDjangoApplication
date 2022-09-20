from django.urls import path
from company import views

# Company Urls

urlpatterns = [
    # path('', views.home, name="home"),
    path('register/', views.register, name='comRegister'),
    # path('delete/', views.delete, name='deleteComp'),
    path('update/', views.update, name='updateComp'),
]
