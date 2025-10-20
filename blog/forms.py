from django import forms
from .models import Author, Category, Post

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'email']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['title']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'category']

class PostSearchForm(forms.Form):
    q = forms.CharField(label="Buscar posts", required=False, max_length=100)
