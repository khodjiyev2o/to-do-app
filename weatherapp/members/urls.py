from . import views
from django.urls import path

urlpatterns = [
    path('',views.index,name='login'),
    path('logout',views.logout_user,name='logout'),
    path('register', views.register_user, name='register'),

    ]