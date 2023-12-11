from django.shortcuts import render, redirect
from account.forms import RegisterForm, ProfileChangeForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm,SetPasswordForm
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib.auth.decorators import login_required
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
        return redirect('profile')
      else:
        messages.error(request,"Failed to login. Please try again")
        return render(request, './account/form.html', {"form": form, "title": "Login page"})
  else:
    form = AuthenticationForm(request)
  return render(request, './account/form.html', {"form": form, "title": "Login page"})



@login_required
def change_password_with_old_password(request):
  if request.method == "POST":
    form = PasswordChangeForm(request.user, request.POST)
    if form.is_valid():
      update_session_auth_hash(request, user=request.user)
      messages.success(request,"Password change successfully!!!")
      return redirect('profile')
  else:
    form = PasswordChangeForm(user=request.user)
  return render(request, './account/form.html', {"form": form, "title": "Password change page"})


@login_required
def change_password_without_old_password(request):
  if request.method == "POST":
    form = SetPasswordForm(request.user, request.POST)
    if form.is_valid():
      update_session_auth_hash(request, user=request.user)
      messages.success(request,"Password change successfully!!!")
      return redirect('profile')
  else:
    form = SetPasswordForm(user=request.user)
  return render(request, './account/form.html', {"form": form, "title": "Password change page"})


@login_required
def change_profile(request):
  if request.method == "POST":
    form = ProfileChangeForm(request.POST, instance=request.user)
    if form.is_valid():
      messages.success(request,"Profile update successfully!!!")
      form.save()
      return redirect('profile')
  else:
    form = ProfileChangeForm(instance=request.user)
  return render(request, './account/form.html', {"form": form, "title": "Profile update"})

      
def logout_user(request):
  messages.success(request, 'Your logout successfully!!!')
  logout(request)
  return redirect('login')