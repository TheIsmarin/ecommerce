# E-commerce

Учебный проект интернет-магазина. Разрабатывается в течение семестра в рамках курса Python-разработки.

## Модули

### `src/models.py`
- `Product` — класс для представления продукта (название, описание, цена, количество)
- `Category` — класс для представления категории (название, описание, список товаров)

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

# Создание категории с продуктом
category = Category("Электроника", "Техника", [product])

print(category.name)  # Электроника
print(category.products)  # [Product(...)]

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
## ������

������ � ����������.
