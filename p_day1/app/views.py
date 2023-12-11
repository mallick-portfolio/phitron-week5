from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from posts.models import Post
# Create your views here.
def home(request):
  posts = Post.objects.all()
  return render(request, './home.html', {"posts": posts})

@login_required
def profile(request):
  return render(request, './profile.html')