from django.db import models

NULLABLE = {"blank": True, "null": True}


class Product(models.Model):
    manufactured_at = models.DateField(
        verbose_name="Дата производства продукта",
        blank=True,
        null=True,
    )
    updated_at = models.DateField(
        verbose_name="Дата последнего изменения в базе данных",
        auto_now=True
    )
    created_at = models.DateField(
        verbose_name="Дата записи в базу данных",
        auto_now_add=True
    )
    product_description = models.TextField(
        verbose_name="Описание товара",
        help_text="Опишите продукт",
        null=True,
        blank=True,
    )
    preview = models.ImageField(
        upload_to='img',
        blank=True,
        null=True,
        verbose_name="Фото товара",
    )
    category = models.ForeignKey(
        "Category",
        on_delete=models.PROTECT,
        verbose_name="Категория",
        help_text="Введите название категории",
        related_name="products",
        max_length=100,
    )
    price = models.IntegerField(
        verbose_name="Цена", help_text="Цена в рублях"
    )
    product_name = models.CharField(
        max_length=100, verbose_name="Название продукта", help_text="Введите наименование продукта", blank=True,
    )

    def __str__(self):
        return self.product_name

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["category", "product_name", "product_description", "price"]


class Category(models.Model):
    description = models.TextField(
        verbose_name="Описание категории",
        blank=True,
        null=True,
    )
    name = models.CharField(
        max_length=100,
        verbose_name="Название категории",
        help_text="Выберите категорию",
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Blog(models.Model):
    heading = models.TextField(
        max_length=100,
        verbose_name="Заголовок"
    )
    slug = models.CharField(
        max_length=100,
        verbose_name="Содержимое",
        unique=True,
    )
    content = models.TextField(
        verbose_name="Содержимое"
    )
    preview = models.ImageField(
        upload_to='img',
        blank=True,
        null=True,
        verbose_name="Фото товара",
    )
    count_views = models.PositiveIntegerField(
        verbose_name="количество просмотров",
        default=0
    )
    date_of_creation = models.DateTimeField(
        verbose_name="дата создания",
        auto_now_add=True
    )
    sing_of_publication = models.BooleanField(
        verbose_name="признак публикации",
        default=True
    )


class Contact(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Имя"
    )
    phone_number = models.CharField(
        max_length=100,
        verbose_name="Номер телефона",
    )
    message = models.TextField(
        verbose_name="Сообщение"
    )


class Version(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='versions'
    )
    number = models.PositiveIntegerField(
        verbose_name="номер версии",
    )
    name = models.TextField(
        max_length=100,
        verbose_name="название версии"
    )
    current_version = models.BooleanField(
        verbose_name="признак текущей версии",
        default=True
    )

    class Meta:
        verbose_name = "Версия"
        verbose_name_plural = "Версии"

    def save(self, *args, **kwargs):
        """ Метод устанавливает все остальные версии продуктов как НЕ текущие"""
        if self.current_version:
            Version.objects.filter(product=self.product, current_version=True).update(current_version=False)
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.number)
