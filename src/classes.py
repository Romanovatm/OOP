class Product:
    """Класс, описывающий продукт"""

    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        """Метод для инициализации класса Product"""

        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, info: dict) -> Product:
        """
        Класс-метод, который принимает на вход параметры товара в словаре и возвращает объект
        класса Product
        """
        return cls(
            name=str(info.get("name", "")),
            description=str(info.get("description", "")),
            price=float(info.get("price", 0)),
            quantity=int(info.get("quantity", 0)),
        )

    @property
    def price(self) -> float:
        """Геттер для получения значения цены"""
        return self.__price

    @price.setter
    def price(self, price: float) -> None:
        """Сеттер для проверки корректной цены товара"""
        if price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = price


class Category:
    """Класс, описывающий категорию"""

    name: str
    description: str
    __products: list[Product]

    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, products: list[Product]) -> None:
        """Метод для инициализации Category"""

        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.product_count += len(products)

    def add_product(self, product: Product) -> None:
        """Метод для добавления продукта в список товаров"""
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        """Геттер для получения списка товаров в категории"""
        return "".join(
            f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n" for product in self.__products
        )
