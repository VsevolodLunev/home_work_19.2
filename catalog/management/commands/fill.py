from django.core.management import BaseCommand
import json

from catalog.models import Product, Category


class Command(BaseCommand):

    @staticmethod
    def json_read_categories():
        with open(file="catalog_data.json", encoding="UTF-8") as file:
            category = json.load(file)
        return category

    @staticmethod
    def json_read_products():
        with open(file="catalog_data.json", encoding="UTF-8") as file:
            product = json.load(file)
        return product

    def handle(self, *args, **options):

        Product.objects.all().delete()
        Category.objects.all().delete()

        # Создайте списки для хранения объектов
        product_for_create = []
        category_for_create = []

        # Обходим все значения категорий из фиктсуры для получения информации об одном объекте
        for category in Command.json_read_categories():
            if category["model"] == "catalog.category":
                category_for_create.append(
                    Category(pk=category['pk'], name=category["fields"]["name"], description=category["fields"]["description"]))

        # Создаем объекты в базе с помощью метода bulk_create()
        Category.objects.bulk_create(category_for_create)

        # Обходим все значения продуктов из фиктсуры для получения информации об одном объекте
        for product in Command.json_read_products():
            if product["model"] == "catalog.product":
                product_for_create.append(
                    Product(name=product["fields"]["name"], manufactured_at=product["fields"]["manufactured_at"],
                            updated_at=product["fields"]["updated_at"], created_at=product["fields"]["created_at"],
                            description=product["fields"]["description"],
                            preview=product["fields"]["preview"],
                            price=product["fields"]["price"],
                            # получаем категорию из базы данных для корректной связки объектов
                            category=Category.objects.get(pk=product["fields"]["category"])))

            # Создаем объекты в базе с помощью метода bulk_create()
        Product.objects.bulk_create(product_for_create)
