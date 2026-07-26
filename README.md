# OOP — каталог товаров

Учебный проект на Python, демонстрирующий основные возможности
объектно-ориентированного программирования на примере товаров и категорий
интернет-магазина.

## Возможности

- создание товаров и категорий;
- создание товара из словаря через классовый метод;
- получение и изменение цены через property;
- проверка новой цены на положительное значение;
- добавление товаров в категорию;
- подсчёт созданных категорий и добавленных товаров;
- вывод товара и категории в удобном строковом формате;
- сложение товаров с расчётом общей стоимости их остатков.

## Основные классы

### `Product`

Описывает товар и хранит:

- название;
- описание;
- цену;
- количество на складе.

Цена находится в приватном атрибуте `__price` и доступна через свойство
`price`. Нулевое или отрицательное значение не устанавливается.

### `Category`

Описывает категорию товаров и хранит:

- название;
- описание;
- приватный список товаров.

Классовые атрибуты:

- `Category.category_count` — количество созданных категорий;
- `Category.product_count` — количество товаров, добавленных в категории.

## Требования

- Python 3.14 или новее;
- Poetry 2.x.

## Установка

Клонируйте репозиторий:

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

print(phone)
```

Результат:

```text
Смартфон, 79990.0 руб. Остаток: 5 шт.
```

### Создание товара из словаря

```python
product_data = {
    "name": "Ноутбук",
    "description": "Ноутбук для работы и учёбы",
    "price": 99990,
    "quantity": 3,
}

laptop = Product.new_product(product_data)
```

Если нужного ключа в словаре нет, метод использует значение по умолчанию.

### Изменение цены

```python
laptop.price = 105000  # цена изменится
laptop.price = 0       # цена не изменится
```

При установке нулевой или отрицательной цены программа выводит сообщение:

```text
Цена не должна быть нулевая или отрицательная
```

### Сложение товаров

Оператор `+` возвращает суммарную стоимость всех единиц двух товаров:

```python
phone = Product("Смартфон", "OLED-дисплей", 79990.0, 2)
case = Product("Чехол", "Силиконовый чехол", 1990.0, 3)

total = phone + case
print(total)
```

Расчёт выполняется по формуле:

```text
цена первого × количество первого + цена второго × количество второго
```

### Работа с категорией

```python
from src.classes import Category, Product

phone = Product("Смартфон", "OLED-дисплей", 79990.0, 5)
category = Category(
    name="Электроника",
    description="Смартфоны, ноутбуки и другая техника",
    products=[phone],
)

headphones = Product(
    "Наушники",
    "Беспроводные наушники",
    12990.0,
    10,
)
category.add_product(headphones)

print(category.products)
print(category)
```

Свойство `products` возвращает строку со всеми товарами категории. Строковое
представление категории показывает общее количество единиц товаров.

## Тестирование

Запуск всех тестов:

```bash
poetry run pytest
```

Запуск с отчётом о покрытии:

```bash
poetry run pytest --cov=src --cov-report=term-missing
```

Для создания HTML-отчёта:

```bash
poetry run pytest --cov=src --cov-report=html
```

Отчёт будет сохранён в каталоге `htmlcov`.

## Проверка качества кода

Проект использует Black, isort, Flake8 и mypy:

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
│   └── test_classes.py   # тесты классов
├── .flake8               # настройки Flake8
├── .gitignore
├── main.py               # точка входа для дальнейшего расширения
├── poetry.lock
├── pyproject.toml
└── README.md
```

## Автор

[Romanovatm](https://github.com/Romanovatm)
