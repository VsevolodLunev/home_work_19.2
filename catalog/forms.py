from django.forms import BooleanField
from django import forms
#from unidecode import unidecode

from .models import Product, Blog


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (
            field_name,
            field,
        ) in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs["class"] = "form-check-input"
            else:
                field.widget.attrs["class"] = "form-class"


class ProductForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"

    def clean_product_name(self):
        clean_data = self.cleaned_data.get('product_name', '')

        words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

        for word in words:
            if word in clean_data.lower():
                raise forms.ValidationError("В названии недопустимое слово")

        return clean_data

    def clean_product_description(self):
        clean_data = self.cleaned_data.get('product_description', '')

        words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

        for word in words:
            if word in clean_data.lower():
                raise forms.ValidationError("В описании недопустимое слово")

        return clean_data


class BlogForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['heading', 'content', 'slug', 'preview', 'sing_of_publication']


class VersionForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"