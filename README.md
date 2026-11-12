# E-commerce

Учебный проект интернет-магазина. Разрабатывается в течение семестра в рамках курса Python-разработки.

## Модули

### `src/models.py`
- `CreationLoggerMixin` — миксин для логирования создания объектов
- `BaseProduct` — абстрактный базовый класс для всех продуктов
- `Product` — класс продукта (наследник `CreationLoggerMixin` и `BaseProduct`, приватная цена, геттер/сеттер, класс-метод `new_product`, магические методы `__str__` и `__add__`)
- `Smartphone` — наследник `Product` (атрибуты: `efficiency`, `model`, `memory`, `color`)
- `LawnGrass` — наследник `Product` (атрибуты: `country`, `germination_period`, `color`)
- `Category` — категория (приватный список товаров, метод `add_product` с проверкой типа, геттер `products`, магический метод `__str__`)

### `src/main.py`
- Демонстрация работы классов: создание продуктов, сложение, добавление в категорию, обработка ошибок

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
from src.models import Category, LawnGrass, Product, Smartphone

# Создание продукта (миксин логирует создание)
product = Product("Телефон", "Смартфон", 50000.0, 10)
# Вывод: Создан объект Product с параметрами: ('Телефон', 'Смартфон', 50000.0, 10), {}
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

# Наследники Product
phone = Smartphone("Samsung", "Флагман", 100000.0, 5, 95.5, "S23", 256, "Чёрный")
grass = LawnGrass("Трава", "Элитная", 500.0, 20, "Россия", "7 дней", "Зелёный")

# Сложение разных типов — TypeError
try:
    phone + grass
except TypeError:
    print("Нельзя складывать разные типы продуктов")

# Добавление не-продукта — TypeError
try:
    category.add_product("Not a product")
except TypeError:
    print("Можно добавлять только продукты или их наследников")

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

- `tests/test_models.py` — тесты для классов `Product`, `Smartphone`, `LawnGrass`, `Category`