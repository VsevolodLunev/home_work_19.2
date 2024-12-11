from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.views.decorators.cache import cache_page
from catalog.apps import CatalogConfig
from catalog.views import (IndexView, ProductDetailView, ContactView, ProductCreateView, ProductListView,
                           ProductUpdateView, ProductDeleteView, VersionCreateView, VersionUpdateView,
                           VersionDeleteView, CategoryListView, CategoryCreateView)
from . import views

app_name = CatalogConfig.name

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('contact/', ContactView.as_view(), name='contact'),
    path("<int:pk>/", cache_page(60)(ProductDetailView.as_view()), name="product_detail"),
    path('create/', ProductCreateView.as_view(), name='product_create'),
    path('list/', ProductListView.as_view(), name='list_product'),
    path('edit_product/<int:pk>', ProductUpdateView.as_view(), name='edit_product'),
    path('delete_product/<int:pk>', ProductDeleteView.as_view(), name='delete_product'),
    path("create_category/", CategoryCreateView.as_view(), name="category_create"),
    path("categories/", CategoryListView.as_view(), name="category_list"),
    path('product/create_version/', VersionCreateView.as_view(), name='version_create'),
    path('edit_version/<int:pk>', VersionUpdateView.as_view(), name='edit_version'),
    path('delete_version/<int:pk>', VersionDeleteView.as_view(), name='delete_version'),
    path('toggle-published-product/<int:pk>/', views.toggle_publish_product, name='toggle_publish_product'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
