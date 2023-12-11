from django.shortcuts import render, redirect
from posts.forms import PostForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def create_post(request):
  if request.method == "POST":
    form = PostForm(request.POST, request.FILES)
    if form.is_valid():
      form.instance.author = request.user
      messages.success(request, "New post created Successfully")
      form.save(commit=True)
      return redirect('profile')
    else:
      messages.error(request, "Failed to create new post")
      return redirect('profile')
  else:
    form = PostForm()
  return render(request, './posts/form.html', {"form": form, "title": "Post Page"})
    
    
      