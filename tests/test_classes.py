from src.classes import Category, Product


def test_product():
    product = Product("яблоко", "красное", 44.5, 10)
    assert product.name == "яблоко"
    assert product.description == "красное"
    assert product.price == 44.5
    assert product.quantity == 10


def test_new_product():
    dict_ = {"name": "апельсин", "description": "красный", "price": 99, "quantity": 5}
    product = Product.new_product(dict_)
    assert product.name == "апельсин"
    assert product.description == "красный"
    assert product.price == 99
    assert product.quantity == 5


def test_price_setter(capsys):
    product = Product("яблоко", "красное", 44.5, 10)
    assert product.price == 44.5
    product.price = 99
    assert product.price == 99
    product.price = 0
    assert product.price == 99
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out


def test_category():
    product = Product("яблоко", "красное", 44.5, 10)
    category = Category("фрукты", "сезонные", [product])
    assert category.name == "фрукты"
    assert category.description == "сезонные"
    assert category.products == "яблоко, 44.5 руб. Остаток: 10 шт.\n"

    assert Category.category_count == 1
    assert Category.product_count == 1


def test_add_product():
    Category.product_count = 0

    product1 = Product("яблоко", "красное", 44.5, 10)
    product2 = Product("апельсин", "красный", 120, 89)

    category = Category("Фрукты", "Свежие фрукты", [])
    category.add_product(product1)

    assert category.products == "яблоко, 44.5 руб. Остаток: 10 шт.\n"
    assert Category.product_count == 1
    category.add_product(product2)
    assert category.products == "яблоко, 44.5 руб. Остаток: 10 шт.\nапельсин, 120 руб. Остаток: 89 шт.\n"
    assert Category.product_count == 2
