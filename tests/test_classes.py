import pytest

from src.classes import Category, LawnGrass, Product, Smartphone


def test_product(capsys):
    product = Product("яблоко", "красное", 44.5, 10)
    message = capsys.readouterr()
    assert message.out == "Product(яблоко, красное, 44.5, 10)\n"
    assert product.name == "яблоко"
    assert product.description == "красное"
    assert product.price == 44.5
    assert product.quantity == 10
    with pytest.raises(ValueError, match="Товар с нулевым количеством не может быть добавлен"):
        Product("яблоко", "красное", 44.5, 0)


def test_product_str():
    product = Product("яблоко", "красное", 44.5, 10)
    assert str(product) == "яблоко, 44.5 руб. Остаток: 10 шт."


def test_product_add():
    product1 = Product("яблоко", "красное", 44.5, 10)
    product2 = Product("апельсин", "красный", 120, 89)
    product3 = Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )
    assert product1 + product2 == 11125
    with pytest.raises(TypeError):
        product1 + product3


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


def test_middle_price_without_products():
    category = Category("фрукты", "сезонные", [])
    assert category.middle_price() == 0


def test_middle_price_with_products():
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category("Смартфоны", "Категория смартфонов", [product1, product2, product3])

    assert category1.middle_price() == 140333.33333333334


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

    with pytest.raises(TypeError):
        category.add_product("Hello World")


def test_category_str():
    product = Product("яблоко", "красное", 44.5, 10)
    category = Category("Фрукты", "Свежие фрукты", [product])
    assert str(category) == "Фрукты, количество продуктов: 10 шт."


def test_smartphone_from_product():

    smartphone1 = Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )

    assert smartphone1.efficiency == 95.5
    assert smartphone1.model == "S23 Ultra"
    assert smartphone1.memory == 256
    assert smartphone1.color == "Серый"


def test_smartphone_from_product_init():

    smartphone1 = Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )

    assert issubclass(type(smartphone1), Product)


def test_lawngrass_from_product():

    grass1 = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")

    assert grass1.country == "Россия"
    assert grass1.germination_period == "7 дней"
    assert grass1.color == "Зеленый"


def test_lawngrass_from_product_init():

    grass1 = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")

    assert issubclass(type(grass1), Product)
