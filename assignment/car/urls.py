
from django.urls import path
from car import views
urlpatterns = [
    path('<int:id>/', views.car_details, name="car_details"),
    path('buy/<int:car_id>/', views.buy_car, name="buy_car"),
]
