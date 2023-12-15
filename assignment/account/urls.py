
from django.urls import path
from account import views
urlpatterns = [
    path('register/', views.register_user, name="register"),
    path('login/', views.login_user, name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('change-password/', views.change_password_with_old_password, name="change-password"),
    path('change-profile/', views.change_profile, name="change_profile"),
    path('change-password/', views.change_password_with_old_password, name="change-password"),
    path('change-password2/', views.change_password_without_old_password, name="change-password2"),
]
