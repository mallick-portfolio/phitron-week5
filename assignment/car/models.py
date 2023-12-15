from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Brand(models.Model):
  name = models.CharField(max_length=20)


class Car(models.Model):
  title = models.CharField(max_length=200)
  description = models.TextField()
  price = models.FloatField()
  image = models.ImageField(upload_to='images/')
  brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True, blank=True, related_name="brands")
  quantity = models.IntegerField(blank=True, null=True)

  def __str__(self) -> str:
    return self.title
  
class Order(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE,related_name="users")
  car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name="cars")

class Comment(models.Model):
  car = models.ForeignKey(Car, on_delete=models.CASCADE)
  name = models.CharField(max_length=50)
  comment = models.TextField(null=True, blank=True)
  
