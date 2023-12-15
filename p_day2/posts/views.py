from django.shortcuts import render, redirect
from posts.forms import PostForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from posts.models import Post
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

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
  
class PostCreateView(CreateView):
  model = Post
  form_class = PostForm
  template_name = './posts/form.html'
  success_url = reverse_lazy('profile')
  def form_valid(self, form):
    form.instance.author = self.request.user
    self.object = form.save()
    return super().form_valid(form)

@login_required
def edit_post(request, id):
  post = Post.objects.get(pk=id)
  if request.method == "POST":
    form = PostForm(request.POST, request.FILES, instance=post)
    if form.is_valid():
      form.instance.author = request.user
      messages.success(request, "Post edit Successfully")
      form.save(commit=True)
      return redirect('profile')
    else:
      messages.error(request, "Failed to edit  post")
      return redirect('profile')
  else:
    form = PostForm(instance=post)
  return render(request, './posts/form.html', {"form": form, "title": "Edit Post Page"})
    
    
class PostEditView(UpdateView):
  model = Post
  form_class = PostForm
  pk_url_kwarg = 'id'
  template_name = './posts/form.html'
  success_url = reverse_lazy('profile')


class PostDeleteView(DeleteView):
  model = Post
  pk_url_kwarg = 'id'
  template_name = './posts/form.html'
  success_url = reverse_lazy('profile')
