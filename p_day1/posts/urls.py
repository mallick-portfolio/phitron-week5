

from django.urls import path
from posts import views
urlpatterns = [
    path('create/', views.create_post, name="create-post"),
]
