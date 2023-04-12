import pytest
import faker_commerce
import factory
from faker import Faker
from products.models import Product, Category
from pytest_factoryboy import register

fake = Faker("pl_PL")
fake.add_provider(faker_commerce.Provider)


@pytest.fixture
def product_onion():
    """Fixture for create product_onion without saving to database
    :return: Object of class Product representing a row in table
    :rtype: Product

    """
    name = "Polish Onion"
    return Product(
        name=name,
        description=fake.sentence(),
        price=fake.ecommerce_price(),
        image=fake.file_name(category="image", extension="png"),
        stock_count=fake.unique.random_int(min=1, max=100),
        barcode=fake.ean(length=13),
    )


@pytest.fixture
def product_db(product_onion, db):
    """Fixture for create product_onion
    :param product_onion:
    :param db: DB  fixture adds database handling
    :return: Object of class Product representing a row in table
    :rtype: Product

    """
    product_onion.save()
    return product_onion


@pytest.fixture
def api_rf():
    from rest_framework.test import APIRequestFactory

    return APIRequestFactory()


@register
class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "products.Product"

    name = factory.Sequence(lambda n: f"{factory.Faker('sentence', nb_words=3)} {n}")
    description = factory.Faker("paragraph")
    price = factory.Faker("pydecimal", left_digits=2, right_digits=2, positive=True, min_value=10, max_value=34)
    image = factory.Faker("image_url")
    stock_count = factory.Faker("pyint", min_value=1, max_value=50)
    barcode = factory.Faker("ean13")


@pytest.fixture
def products_batch(db):
    return ProductFactory.create_batch(60)


@pytest.fixture
def category_db(db):
    return Category.objects.create(name="Potato")
