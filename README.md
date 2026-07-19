# Проект по объектно-ориентированному программированию

Учебный Python-проект, демонстрирующий основы объектно-ориентированного программирования на примере товаров и категорий интернет-магазина.

## Реализованные классы

### `Product`

Класс описывает товар и хранит следующие данные:

- `name` — название товара;
- `description` — описание товара;
- `price` — цена;
- `quantity` — количество товара в наличии.

Пример создания товара:

```python
from src.classes import Product

product = Product(
    name="Смартфон",
    description="Смартфон с OLED-дисплеем",
    price=79990.0,
    quantity=5,
)
```

### `Category`

Класс описывает категорию товаров и хранит:

- `name` — название категории;
- `description` — описание категории;
- `products` — список объектов `Product`;
- `category_count` — общее количество созданных категорий;
- `product_count` — общее количество товаров во всех созданных категориях.

Пример создания категории:

```python
from src.classes import Category, Product

product = Product("Смартфон", "Смартфон с OLED-дисплеем", 79990.0, 5)
category = Category("Электроника", "Смартфоны и другая техника", [product])

print(category.name)
print(Category.category_count)
print(Category.product_count)
```

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

Poetry создаст виртуальное окружение и установит зависимости, зафиксированные в `poetry.lock`.

## Использование

Классы можно импортировать из модуля `src.classes`:

```python
from src.classes import Category, Product

apple = Product("Яблоко", "Красное яблоко", 44.5, 10)
fruits = Category("Фрукты", "Сезонные фрукты", [apple])

print(fruits.name)          # Фрукты
print(fruits.products)      # список товаров категории
print(Category.category_count)
print(Category.product_count)
```

Файл `main.py` оставлен пустым, поэтому проект используется через импорт классов или интерактивную консоль Python.

## Тестирование

Запуск всех тестов:

```bash
poetry run pytest
```

Запуск тестов с измерением покрытия:

```bash
poetry run pytest --cov=src --cov-report=term-missing
```

Тесты проверяют корректность инициализации объектов `Product` и `Category`, а также работу счётчиков категорий и товаров.

## Проверка качества кода

В проекте настроены Black, isort, Flake8 и mypy:

```bash
poetry run black --check .
poetry run isort --check-only .
poetry run flake8 src tests main.py
poetry run mypy src main.py
```

Для автоматического форматирования:

```bash
poetry run black .
poetry run isort .
```

## Структура проекта

```text
OOP/
├── src/
│   ├── __init__.py
│   └── classes.py          # классы Product и Category
├── tests/
│   ├── __init__.py
│   └── test_classes.py     # тесты классов
├── .flake8                 # настройки Flake8
├── .gitignore
├── main.py                 # точка входа, пока не реализована
├── poetry.lock             # зафиксированные версии зависимостей
└── pyproject.toml          # метаданные и настройки проекта
```

## Автор

[Romanovatm](https://github.com/Romanovatm)
