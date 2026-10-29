"""Тесты для моделей."""

import pytest

from src.models import Category, Product


@pytest.fixture
def product():
    """Фикстура с продуктом."""
    return Product("Телефон", "Смартфон", 50000.0, 10)


@pytest.fixture
def category(product):
    """Фикстура с категорией."""
    return Category("Электроника", "Техника", [product])


def test_product_init(product):
    """Тест инициализации продукта."""
    assert product.name == "Телефон"
    assert product.description == "Смартфон"
    assert product.price == 50000.0
    assert product.quantity == 10


def test_category_init(category, product):
    """Тест инициализации категории."""
    assert category.name == "Электроника"
    assert category.description == "Техника"


def test_category_count():
    """Тест подсчёта категорий."""
    initial = Category.category_count
    Category("Новая", "Описание", [])
    assert Category.category_count == initial + 1


def test_product_count(product):
    """Тест подсчёта продуктов."""
    initial = Category.product_count
    Category("Новая", "Описание", [product, product])
    assert Category.product_count == initial + 2


def test_add_product(category):
    """Тест добавления продукта."""
    initial = Category.product_count
    new_product = Product("Ноутбук", "Игровой", 100000.0, 5)
    category.add_product(new_product)
    assert Category.product_count == initial + 1


def test_products_getter(category, product):
    """Тест геттера products."""
    result = category.products
    assert "Телефон" in result
    assert "50000.0 руб." in result
    assert "Остаток: 10 шт." in result


def test_new_product():
    """Тест класс-метода new_product."""
    data = {
        "name": "Ноутбук",
        "description": "Игровой",
        "price": 100000.0,
        "quantity": 5,
    }
    product = Product.new_product(data)
    assert product.name == "Ноутбук"
    assert product.price == 100000.0


def test_price_setter_positive(product):
    """Тест сеттера цены (положительное значение)."""
    product.price = 60000.0
    assert product.price == 60000.0


def test_price_setter_negative(product, capsys):
    """Тест сеттера цены (отрицательное значение)."""
    product.price = -100
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert product.price == 50000.0


def test_price_setter_zero(product, capsys):
    """Тест сеттера цены (ноль)."""
    product.price = 0
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert product.price == 50000.0
