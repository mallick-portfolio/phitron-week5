from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from posts.models import Post, Category
# Create your views here.
def home(request, category_slug = None):
  if category_slug:
    posts = Post.objects.filter(category__slug =category_slug)
  else:
    posts = Post.objects.all()
  categories = Category.objects.all()
  return render(request, './home.html', {"posts": posts ,"categories": categories})

@login_required
def profile(request):
  posts = Post.objects.filter(author=request.user)
  print(posts)
  return render(request, './profile.html', {"posts": posts})

def post_details(request, id):
  post = Post.objects.filter(id=id).first()
  return render(request, './details.html', {"post": post})