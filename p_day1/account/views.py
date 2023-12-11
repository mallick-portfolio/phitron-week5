from django.shortcuts import render, redirect
from account.forms import RegisterForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm,SetPasswordForm
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
# Create your views here.


def register_user(request):
  if request.method == "POST":
    form = RegisterForm(request.POST)
    if form.is_valid():
      messages.success(request, "Registe user successfully!!!")
      form.save()
      return redirect('home')
  else:
    form = RegisterForm()
  return render(request, './account/form.html', {"form": form, "title": "Register page"})

def login_user(request):
  if request.method == "POST":
    form = AuthenticationForm(request, request.POST)
    if form.is_valid():
      username = form.cleaned_data['username']
      password = form.cleaned_data['password']
      user = authenticate(username=username, password=password)
      if user is not None:
        messages.success(request,"Login successfully!!!")
        login(request, user=user)
        return redirect('home')
      else:
        messages.error(request,"Failed to login. Please try again")
        return render(request, './account/form.html', {"form": form, "title": "Login page"})
  else:
    form = AuthenticationForm(request)
  return render(request, './account/form.html', {"form": form, "title": "Login page"})

      
def logout_user(request):
  messages.success(request, 'Your logout successfully!!!')
  logout(request)
  return redirect('login')