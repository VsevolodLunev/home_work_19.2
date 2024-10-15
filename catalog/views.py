from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator

from catalog.forms import ProductForm
from catalog.models import Product


def home(request):
    products = Product.objects.all()
    paginator = Paginator(products, 4)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, 'catalog/product.html', {"page_obj": page_obj})


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f"{name} ({phone}): {message}")
    return render(request, 'catalog/contacts.html')


def info_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, "catalog/info_product.html", {"product": product})


def create_product(request):
    request.method = 'POST'
    form = ProductForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return redirect("catalog:home")
    return render(request, "catalog/create_products.html", {"form": form})


def buy_product(request):
    buy = Product.objects.all()
    return render(request, "catalog/buy_product.html", {"buy": buy})
