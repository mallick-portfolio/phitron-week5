from django.shortcuts import render, redirect
from car import models
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from car.forms import CommentForm
# Create your views here.

def car_details(request, id):
  car = models.Car.objects.filter(id=id).first()
  if request.method == "POST":
    form = CommentForm(request.POST)
    if form.is_valid():
      form.instance.car = car
      form.save()
      messages.success(request, "Comment added successfully")
      form = CommentForm()
      return render(request, 'car_details.html', {"car": car,"form": form})
  else:
    form = CommentForm()
    print(form)
  return render(request, 'car_details.html', {"car": car, "form": form})


@login_required
def buy_car(request, car_id = None):
  car = models.Car.objects.filter(id=car_id).first()
  if car is not None:
    car.quantity = car.quantity - 1
    car.save()
    order = models.Order.objects.create(user=request.user, car=car)
    order.save()
    messages.success(request, "Order confirm successfully")
    return render(request, 'car_details.html', {"car": car})
  else:
    messages.error(request, "No Car found with the selected id")
    return render(request, 'car_details.html', {"car": car})
