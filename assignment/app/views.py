from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from car.models import Car, Brand, Order
from django.views.generic import ListView
from car import forms
from django.contrib import messages
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

@login_required
def create_car(request):
  carform = forms.CarForm()
  if request.method == "POST":
    carform = forms.CarForm(request.POST)
    if carform.is_valid():
      carform.save()
      messages.success(request, 'Car created successfully')
      return render()


@method_decorator(login_required, name='dispatch')
class OrderListView(ListView):
  model = Order
  template_name = './profile.html'
  def get_context_data(self, *args, **kwargs):
    context = super(OrderListView, self).get_context_data(*args, **kwargs)
    orders = Order.objects.filter(user=self.request.user)
    context["orders"] = orders
    return context
