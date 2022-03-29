from django.urls import path
from .import views
urlpatterns = [
    path('main',views.index,name='main'),
    path('<int:pk>/deletecity',views.WeatherDeleteView.as_view(), name='deletecity'),
    path('<int:pk>/deletecar', views.CarDeleteView.as_view(), name='deletecar'),
    path('pricing', views.pricing, name='pricing'),
    path('market', views.market, name='market'),
    path('search', views.search, name='search'),
    path('<int:pk>',views.CarDetailView.as_view(),name='view'),
    path('<int:pk>/update',views.CarUpdateView.as_view(),name='update'),
    path('user_profile',views.user_profile,name='user_profile'),
    path('approval', views.approval, name='approval'),

]
