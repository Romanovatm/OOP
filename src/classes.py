class Product:
    """Класс, описывающий продукт"""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        """Метод для инициализации класса Product"""

        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    """Класс, описывающий категорию"""

    name: str
    description: str
    products: list[Product]

    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, products: list[Product]) -> None:
        """Метод для инициализации Category"""

        self.name = name
        self.description = description
        self.products = products

        Category.category_count += 1
        Category.product_count += len(products)
