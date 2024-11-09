from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import (contacts, ProductCreateView, ProductListView, ProductDetailView,
                           ProductUpdateView, ProductDeleteView, BlogListView, BlogCreateView, BlogUpdateView,
                           BlogDeleteView, BlogDetailView)

app_name = CatalogConfig.name

urlpatterns = [
    path("", ProductListView.as_view(), name="product_list"),
    path("contacts/", contacts, name="contacts"),
    path("<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
    path("create_product/", ProductCreateView.as_view(), name="product_create"),
    path("<int:pk>/update/", ProductUpdateView.as_view(), name="product_update"),
    path("<int:pk>/delete/", ProductDeleteView.as_view(), name="product_delete"),

    path('blog/', BlogListView.as_view(), name='blog_list'),
    path('blog/create/', BlogCreateView.as_view(), name='blog_create'),
    path('<slug:slug>/update/', BlogUpdateView.as_view(), name='update_blog'),
    path('<slug:slug>/delete/', BlogDeleteView.as_view(), name='delete_blog'),
    path('<slug:slug>/view/', BlogDetailView.as_view(), name='detail_blog'),
]
