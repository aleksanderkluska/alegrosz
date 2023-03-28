import pytest

from products.models import Product
from faker import Faker
import faker_commerce

fake = Faker("pl_PL")
fake.add_provider(faker_commerce.Provider)


@pytest.fixture
def product(db):
    """Fixture for create product
    :param db: DB  fixture adds database handling
    :return: Object of class Product representing a row in table
    :rtype: Product

    """
    name = "Polish Onion"
    return Product.objects.create(
        name=name,
        description=fake.sentence(),
        price=fake.ecommerce_price(),
        image=fake.file_name(category="image", extension="png"),
        stock_count=fake.unique.random_int(min=1, max=100),
        barcode=fake.ean(length=13),
    )


def test_correct_gui_representation():
    name = fake.ecommerce_name()

    product = Product(
        name=name,
        description=fake.sentence(),
        price=fake.ecommerce_price(),
        image=fake.file_name(category="image", extension="png"),
        stock_count=fake.unique.random_int(min=1, max=100),
        barcode=fake.ean(length=13),
    )

    assert str(product) == name


def test_auto_slug(product):
    assert product.slug == "polish-onion"


def test_custom_slug(db):
    name = fake.ecommerce_name()

    product = Product(
        name=name,
        description=fake.sentence(),
        price=fake.ecommerce_price(),
        image=fake.file_name(category="image", extension="png"),
        stock_count=fake.unique.random_int(min=1, max=100),
        barcode=fake.ean(length=13),
        slug="test-custom-slug",
    )

    assert product.slug == "test-custom-slug"


@pytest.mark.skip(reason="WIP")
def test_custom_invalid_slug(db):
    name = fake.ecommerce_name()

    product = Product(
        name=name,
        description=fake.sentence(),
        price=fake.ecommerce_price(),
        image=fake.file_name(category="image", extension="png"),
        stock_count=fake.unique.random_int(min=1, max=100),
        barcode=fake.ean(length=13),
        slug="",
    )

    assert product.slug == "test-custom-slug"
