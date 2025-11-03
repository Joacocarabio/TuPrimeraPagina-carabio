from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'subtitle', 'content', 'image']

class PostSearchForm(forms.Form):
    q = forms.CharField(label="Buscar", required=False)
