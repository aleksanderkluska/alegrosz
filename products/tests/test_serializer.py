from products.serializers import ProductSerializer


def test_serializer_all_fields_present(product_db):
    serializer = ProductSerializer(instance=product_db)
    assert tuple(serializer.data.keys()) == (
        "id",
        "name",
        "description",
        "price",
        "image",
        "popularity",
        "rank",
        "barcode",
    )
