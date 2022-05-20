from django.urls import path
from . import views


urlpatterns=[
    path('',views.api_home),
    path('products/', views.products,name="products"),
    path('product_detail/<int:pk>', views.product_detail, name="product_detail"),
    path('product_delete/<int:pk>', views.product_delete, name="product_delete"),
    path('product_update/<int:pk>', views.product_update, name="product_update"),
    path('product_create', views.product_create, name="product_create"),

]