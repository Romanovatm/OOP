from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Базовый класс (шаблон) для создания продуктов"""

    @abstractmethod
    def __init__(self) -> None:
        super().__init__()


class MixinInit:
    """Класс-миксин, который будет при создании объекта, то есть при работе метода __init__ печатает
     в консоль информацию о том, от какого класса и с какими параметрами был создан объект"""

    def __init__(self) -> None:
        print(repr(self))

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.name}, {self.description}, {self.price}, {self.quantity})"  # type: ignore


class Product(BaseProduct, MixinInit):
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
        super().__init__()

    def __str__(self) -> str:
        """Метод возвращает текстовое представление объекта для пользователя."""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: Product) -> float:
        """Складывает сумму всех продуктов из списка товара"""
        if type(self) is type(other):
            result = self.quantity * self.price + other.quantity * other.price
        else:
            raise TypeError
        return result

    @classmethod
    def new_product(cls, info: dict) -> Product:
        """Класс-метод, который принимает на вход параметры товара в словаре и возвращает объект
        класса Product"""

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


class Smartphone(Product):
    """Класс, описывающий категорию товаров: Smartphone"""

    name: str
    description: str
    __price: float
    quantity: int
    efficiency: float
    model: str
    memory: int
    color: str

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ) -> None:
        """Метод для инициализации класса Smartphone, наследуемого от класса Product"""

        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    """Класс, описывающий категорию товаров: LawnGrass"""

    name: str
    description: str
    __price: float
    quantity: int
    country: str
    germination_period: str
    color: str

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ) -> None:
        """Метод для инициализации класса LawnGrass, наследуемого от класса Product"""

        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color


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

    def __str__(self) -> str:
        """Метод возвращает текстовое представление объекта для пользователя"""

        return f"{self.name}, количество продуктов: {sum(product.quantity for product in self.__products)} шт."

    def add_product(self, product: Product) -> None:
        """Метод для добавления продукта в список товаров"""

        if isinstance(product, Product) or issubclass(type(product), Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError

    @property
    def products(self) -> str:
        """Геттер для получения списка товаров в категории"""

        return "".join(f"{str(product)}\n" for product in self.__products)
