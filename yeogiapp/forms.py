from django import forms
from .models import Post, Comment

class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', 'spacePhoto']

class CommentModelForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']        