from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import home, contacts, info_product, create_product, buy_product

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('product/<int:pk>/', info_product, name='info_product'),
    path('create/', create_product, name='create_product'),
    path('buy_product/', buy_product, name="buy_product")
]
