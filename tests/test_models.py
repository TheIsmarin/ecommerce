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
    assert category.products == [product]


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
