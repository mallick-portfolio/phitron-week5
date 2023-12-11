from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
  name = models.CharField(max_length=50)
  slug = models.SlugField(max_length=50)

  def __str__(self) -> str:
    return self.name


class Post(models.Model):
  title = models.CharField(max_length=200)
  description = models.TextField()
  image = models.ImageField(upload_to='images/')
  category = models.ManyToManyField(Category)
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)

