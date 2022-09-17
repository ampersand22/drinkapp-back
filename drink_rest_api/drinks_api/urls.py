from django.urls import path
from . import views

urlpatterns = [
    path('api/drinks', views.DrinkList.as_view(), name='drink_list'), 
    path('api/drinks/<int:pk>', views.DrinkDetail.as_view(), name='drink_detail'), 
]