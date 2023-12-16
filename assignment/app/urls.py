from django.urls import path
from app import views
urlpatterns = [
    path("", views.home, name="home"),
    path("profile/", views.OrderListView.as_view(), name="profile"),
    # path("profile/", views.profile, name="profile"),
    path("brand/<slug:brand_name>/", views.home, name="brand_name"),
]
