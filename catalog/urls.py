from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import (ContactsListView, CreateProductListView, ProductListView, ProductDetailView,
                           ProductUpdateView, BlogListView, BlogCreateView, BlogUpdateView,
                           BlogDeleteView, BlogDetailView)

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('contacts/', ContactsListView.as_view(), name='contacts'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('create/', CreateProductListView.as_view(), name='create_product'),
    path('product/<int:pk>/update', ProductUpdateView.as_view(), name="product_update"),

    path('blog/', BlogListView.as_view(), name='blog_list'),
    path('blog/create/', BlogCreateView.as_view(), name='blog_create'),
    path('<slug:slug>/update/', BlogUpdateView.as_view(), name='update_blog'),
    path('<slug:slug>/delete/', BlogDeleteView.as_view(), name='delete_blog'),
    path('<slug:slug>/view/', BlogDetailView.as_view(), name='detail_blog'),
]
