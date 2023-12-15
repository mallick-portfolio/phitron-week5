from django.urls import path
from app import views
urlpatterns = [
    path("", views.home, name="home"),
    path("profile/", views.profile, name="profile"),
    # path("post-details/<int:id>/", views.post_details, name="post_details"),
    path("brand/<slug:brand_name>/", views.home, name="brand_name"),
]
