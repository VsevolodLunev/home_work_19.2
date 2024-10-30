from django.forms import BooleanField
from django import forms
#from unidecode import unidecode

from .models import Product, Version, Blog


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = "form-check-input"
            else:
                field.widget.attrs['class'] = "form-control"


class ProductForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        exclude = ("count_views",)

    def clean_product_name(self):
        clean_data = self.cleaned_data.get('product_name', '')

        words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

        for word in words:
            if word in clean_data.lower():
                raise forms.ValidationError(
                    'Вы не можете использовать запрещенные слова в названии продукта или описании продукта'
                )

        return clean_data

    def clean_product_description(self):
        clean_data = self.cleaned_data.get('product_description', '')

        words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

        for word in words:
            if word in clean_data.lower():
                raise forms.ValidationError(
                    'Вы не можете использовать запрещенные слова в названии продукта или описании продукта'
                )

        return clean_data


class BlogForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['heading', 'content', 'slug', 'preview', 'sing_of_publication']


class VersionForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = "__all__"
        widgets = {
            'version_number': forms.TextInput(attrs={'class': 'form-control'}),
            'version_name': forms.TextInput(attrs={'class': 'form-control'}),
            'is_current': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
