from django import forms
from catalog.models import Product
from catalog.models import Blog


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = {"name", "price", "category", "preview", "description"}


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['heading', 'content', 'slug', 'preview', 'sing_of_publication']
