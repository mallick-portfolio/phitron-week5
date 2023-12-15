

from django.urls import path
from posts import views
urlpatterns = [
    path('create/', views.PostCreateView.as_view(), name="create-post"),
    # path('create/', views.create_post, name="create-post"),
    path('edit/<int:id>', views.PostEditView.as_view(), name="edit-post"),
    path('delete/<int:id>', views.PostDeleteView.as_view(), name="delete-post"),
    # path('edit/<int:id>', views.edit_post, name="edit-post"),
]
