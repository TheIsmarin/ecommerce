# E-commerce

Учебный проект интернет-магазина. Разрабатывается в течение семестра в рамках курса Python-разработки.

## Модули

### `src/models.py`
- `Product` — класс для представления продукта (приватная цена, геттер/сеттер, класс-метод `new_product`, магические методы `__str__` и `__add__`)
- `Category` — класс для представления категории (приватный список товаров, метод `add_product`, геттер `products`, магический метод `__str__`)

## Установка

1. Клонируйте репозиторий:

```
git clone https://github.com/TheIsmarin/ecommerce.git
```

2. Установите зависимости:

```
poetry install
```

## Примеры использования

```python
from src.models import Category, Product

# Создание продукта
product = Product("Телефон", "Смартфон", 50000.0, 10)
print(product)  # Телефон, 50000.0 руб. Остаток: 10 шт.

# Создание категории с продуктом
category = Category("Электроника", "Техника", [product])
print(category)  # Электроника, количество продуктов: 10 шт.

# Класс-метод new_product
new_product = Product.new_product(
    {"name": "Ноутбук", "description": "Игровой", "price": 100000.0, "quantity": 5}
)
print(new_product.price)  # 100000.0

# Сложение продуктов
other = Product("Ноутбук", "Игровой", 100000.0, 5)
print(product + other)  # 50000.0 * 10 + 100000.0 * 5 = 1000000.0

# Счётчики класса
print(Category.category_count)  # 1
print(Category.product_count)  # 1
```

## Тестирование

Проект покрыт тестами с использованием `pytest` и `pytest-cov`.

### Запуск тестов

```
poetry run pytest
```

### Запуск с покрытием

```
poetry run pytest --cov=src --cov-report=html
```

Покрытие: 100%

Отчёт покрытия: `htmlcov/index.html`

### Структура тестов

- `tests/test_models.py` — тесты для классов `Product` и `Category`