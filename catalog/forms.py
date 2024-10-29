from django import forms
from .models import Product
from .models import Blog


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "category", "preview", "description", 'manufactured_at',]


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['heading', 'content', 'slug', 'preview', 'sing_of_publication']
