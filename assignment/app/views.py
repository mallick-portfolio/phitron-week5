from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from car.models import Car, Brand, Order
# Create your views here.
def home(request, brand_name = None):
  brands = Brand.objects.all()
  if brand_name:
    cars = Car.objects.filter(brand__name = brand_name)
  else:
    cars = Car.objects.all()
  return render(request, './home.html', {"cars": cars, "brands": brands})

@login_required
def profile(request):
  orders = Order.objects.filter(user=request.user)
  return render(request, './profile.html',{"orders": orders})

