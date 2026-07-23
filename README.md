# OOP — каталог товаров

Учебный Python-проект, демонстрирующий основные принципы объектно-ориентированного программирования на примере товаров и категорий интернет-магазина.

## Возможности

- создание товаров и категорий;
- создание товара из словаря;
- изменение цены с проверкой корректности;
- добавление товаров в категорию;
- подсчёт созданных категорий и добавленных в них товаров;
- получение форматированного списка товаров категории.

## Требования

- Python 3.14 или новее;
- Poetry 2.x.

## Установка

Клонируйте репозиторий и перейдите в папку проекта:

```bash
git clone https://github.com/Romanovatm/OOP.git
cd OOP
```

Установите зависимости:

```bash
poetry install
```

## Использование

### Создание товара

```python
from src.classes import Product

phone = Product(
    name="Смартфон",
    description="Смартфон с OLED-дисплеем",
    price=79990.0,
    quantity=5,
)

print(phone.name)
print(phone.price)
```

Товар также можно создать из словаря с помощью классового метода `new_product`:

```python
product_data = {
    "name": "Ноутбук",
    "description": "Ноутбук для работы и учёбы",
    "price": 99990,
    "quantity": 3,
}

laptop = Product.new_product(product_data)
```

Цена хранится в приватном атрибуте и доступна через свойство `price`. При попытке установить нулевую или отрицательную цену текущее значение не изменится.

```python
laptop.price = 105000  # цена изменится
laptop.price = 0       # цена не изменится
```

### Работа с категорией

```python
from src.classes import Category, Product

phone = Product("Смартфон", "Смартфон с OLED-дисплеем", 79990.0, 5)
category = Category(
    name="Электроника",
    description="Смартфоны, ноутбуки и другая техника",
    products=[phone],
)

headphones = Product("Наушники", "Беспроводные наушники", 12990.0, 10)
category.add_product(headphones)

print(category.products)
```

Результат:

```text
Смартфон, 79990.0 руб. Остаток: 5 шт.
Наушники, 12990.0 руб. Остаток: 10 шт.
```

Классовые атрибуты `Category.category_count` и `Category.product_count` содержат соответственно количество созданных категорий и общее количество товаров в них.

## Тестирование

Запуск тестов:

```bash
poetry run pytest
```

Запуск тестов с отчётом о покрытии:

```bash
poetry run pytest --cov=src --cov-report=term-missing
```

## Проверка качества кода

В проекте настроены Black, isort, Flake8 и mypy:

```bash
poetry run black --check .
poetry run isort --check-only .
poetry run flake8 src tests main.py
poetry run mypy src main.py
```

Автоматическое форматирование:

```bash
poetry run black .
poetry run isort .
```

## Структура проекта

```text
OOP/
├── src/
│   ├── __init__.py
│   └── classes.py        # классы Product и Category
├── tests/
│   ├── __init__.py
│   └── test_classes.py   # тесты
├── .flake8               # настройки Flake8
├── .gitignore
├── main.py
├── poetry.lock
├── pyproject.toml
└── README.md
```

## Автор

[Romanovatm](https://github.com/Romanovatm)
