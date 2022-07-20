from django.urls import path
from . import views


urlpatterns=[
    path('',views.api_home),
    path('task-list/', views.products,name="tasks"),
    path('task-detail/<str:pk>/', views.product_detail, name="task_detail"),
    path('task-delete/<str:pk>/', views.product_delete, name="task_delete"),
    path('task-update/<str:pk>/', views.product_update, name="task_update"),
    path('task-create/', views.product_create, name="task_create"),

]