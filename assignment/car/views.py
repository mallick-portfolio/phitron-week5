from django.shortcuts import render, redirect
from car import models
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from car.forms import CommentForm
from django.views.generic import DetailView
from django.views import View  
from django.utils.decorators import method_decorator
# Create your views here.


class CarDetailView(DetailView):
  model =  models.Car
  pk_url_kwarg = 'id'
  template_name = 'car_details.html'
  # queryset = models.Car.objects.all()
  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['comments'] = models.Comment.objects.filter(car=self.get_object())
      context['form'] = CommentForm()
      return context
  def post(self, request, *args, **kwargs):
      print("helo world")
      form = CommentForm(request.POST)
      if form.is_valid():
        self.object = self.get_object()
        form.instance.car = self.get_object()
        form.save()
        # messages(self.request, "Comment added successfully")
        context = super(CarDetailView, self).get_context_data(**kwargs)
        context['form'] = CommentForm
        context['comments'] = models.Comment.objects.filter(car=self.get_object())
        return self.render_to_response(context=context)
      else:
          self.object = self.get_object()
          context = super(CarDetailView, self).get_context_data(**kwargs)
          context['form'] = CommentForm()
          return self.render_to_response( context=context)




def car_details(request, id):
  car = models.Car.objects.filter(id=id).first()
  comments = models.Comment.objects.filter(car=car)
  if request.method == "POST":
    form = CommentForm(request.POST)
    if form.is_valid():
      form.instance.car = car
      form.save()
      messages.success(request, "Comment added successfully")
      form = CommentForm()
      return render(request, 'car_details.html', {"car": car,"form": form, "comments":comments})
  else:
    form = CommentForm()
    return render(request, 'car_details.html', {"car": car,"form": form, "comments":comments})


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

@method_decorator(login_required, name='dispatch')
class BuyCarView(View):
   def get(self, request, car_id = None):
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