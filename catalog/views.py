from django.forms import inlineformset_factory
from django.urls import reverse_lazy, reverse
from django.shortcuts import render

from django.utils.text import slugify
from django.views.generic import ListView, TemplateView, CreateView, DetailView, UpdateView, DeleteView

from catalog.forms import VersionForm, ProductForm
from catalog.models import Product, Contact, Blog, Version


def contacts(request):
    return render(request, "catalog/contacts.html")


class ProductListView(ListView):
    model = Product

    def get_context_data(self, *args, object_list=None, **kwargs):
        context_data = super().get_context_data(**kwargs)
        for product in context_data["object_list"]:
            active_version = Version.objects.filter(
                product=product, current_version=True
            ).first()
            product.active_version = active_version
        return context_data


class ProductDetailView(DetailView):
    model = Product

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_counter += 1
        self.object.save()
        return self.object


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')

    def get_success_url(self):
        return reverse("catalog:product_detail", args=[self.kwargs.get("pk")])

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        ProductFormset = inlineformset_factory(Product, Version, VersionForm, extra=1)
        if self.request.method == "POST":
            context_data["formset"] = ProductFormset(
                self.request.POST, instance=self.object
            )
        else:
            context_data["formset"] = ProductFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data["formset"]
        if form.is_valid() and formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(
                self.get_context_data(form=form, formset=formset)
            )


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product_list')


class VersionCreateView(CreateView):
    model = Version
    form_class = VersionForm
    success_url = reverse_lazy("catalog:product_list")


class BlogListView(ListView):
    model = Blog

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(sing_of_publication=True)
        return queryset


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.count_views += 1
        self.object.save()
        return self.object


class BlogCreateView(CreateView):
    model = Blog
    fields = ("heading", "content", "preview", "count_views")
    success_url = reverse_lazy('catalog:blog_list')

    def form_valid(self, form):
        if form.is_valid():
            obj = form.save(commit=False)
            obj.slug = slugify(obj.heading)
            obj.save()
        return super().form_valid(form)


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ("heading", "content", "preview")
    success_url = reverse_lazy("catalog:blog_list")

    def get_success_url(self):
        return reverse('catalog:detail_blog', args=[self.kwargs.get('slug')])


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy("c   atalog:blog_list")

    def get_object(self, queryset=None):
        slug = self.kwargs.get('slug')
        return Blog.objects.get(slug=slug)
