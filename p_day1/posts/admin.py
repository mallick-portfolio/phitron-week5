from django.contrib import admin
from posts.models import Category, Post
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
  prepopulated_fields = {"slug": ("name",)}
  # readonly_fields = ['slug']



admin.site.register(Post)
admin.site.register(Category, CategoryAdmin)