
from django.urls import path
from car import views
urlpatterns = [
    path('<int:id>/', views.CarDetailView.as_view(), name="car_details"),
    # path('<int:id>/', views.car_details, name="car_details"),
    path('buy/<int:car_id>/', views.BuyCarView.as_view(), name="buy_car"),
    # path('buy/<int:car_id>/', views.buy_car, name="buy_car"),
]
