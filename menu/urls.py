from django.urls import path
from . import views

urlpatterns = [
    path('', views.coffee_list, name='coffee_list'),
    path('coffee/<int:pk>/', views.coffee_detail, name='coffee_detail'),
]
