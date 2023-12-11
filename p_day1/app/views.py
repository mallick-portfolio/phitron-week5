from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from posts.models import Post
# Create your views here.
def home(request):
  posts = Post.objects.all()
  return render(request, './home.html', {"posts": posts})

@login_required
def profile(request):
  posts = Post.objects.filter(author=request.user)
  print(posts)
  return render(request, './profile.html', {"posts": posts})

def post_details(request, id):
  post = Post.objects.filter(id=id).first()
  return render(request, './details.html', {"post": post})