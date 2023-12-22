from django import forms
from car.models import Comment, Car


class CommentForm(forms.ModelForm):
  class Meta:
    model = Comment
    fields = "__all__"
    exclude = ['car']

class CarForm(forms.ModelForm):
  class Meta:
    model = Car
    fields = '__all__'
