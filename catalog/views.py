
from django.urls import reverse_lazy, reverse
from django.utils.text import slugify
from django.views.generic import ListView, TemplateView, CreateView, DetailView, UpdateView, DeleteView


from catalog.models import Product, Contact, Blog


class ProductListView(ListView):
    model = Product
    paginate_by = 4


class ContactsListView(TemplateView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object_list"] = Contact.objects.all()
        return context


class ProductDetailView(DetailView):
    model = Product


class CreateProductListView(CreateView):
    model = Product
    fields = ("name", "price", "category", "preview", "description")
    success_url = reverse_lazy('catalog:home')


class ProductUpdateView(UpdateView):
    model = Product
    fields = ("name", "price", "category", "preview", "description")
    success_url = reverse_lazy('catalog:home')


class BlogListView(ListView):
    model = Blog
    queryset = Blog.objects.filter(slug__isnull=False)


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
            obj = form.save()
            obj.slug = slugify(obj.title)
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
    success_url = reverse_lazy("catalog:blog_list")

    def get_object(self, queryset=None):
        slug = self.kwargs.get('slug')
        return Blog.objects.get(slug=slug)
