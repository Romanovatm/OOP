from src.classes import Category, Product


def test_product():
    product = Product("яблоко", "красное", 44.5, 10)
    assert product.name == "яблоко"
    assert product.description == "красное"
    assert product.price == 44.5
    assert product.quantity == 10


def test_category():
    product = Product("яблоко", "красное", 44.5, 10)
    category = Category("фрукты", "сезонные", [product])
    assert category.name == "фрукты"
    assert category.description == "сезонные"
    assert category.products == [product]

    assert Category.category_count == 1
    assert Category.product_count == 1
