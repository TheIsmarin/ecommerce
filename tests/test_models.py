"""Тесты для моделей."""

import pytest

from src.models import BaseProduct, Category, LawnGrass, Product, Smartphone


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


def test_product_str(product):
    """Тест строкового отображения продукта."""
    assert str(product) == "Телефон, 50000.0 руб. Остаток: 10 шт."


def test_category_str(category):
    """Тест строкового отображения категории."""
    assert str(category) == "Электроника, количество продуктов: 10 шт."


def test_product_add(product):
    """Тест сложения продуктов."""
    other = Product("Ноутбук", "Игровой", 100000.0, 5)
    assert product + other == 50000.0 * 10 + 100000.0 * 5


def test_smartphone_init():
    """Тест инициализации смартфона."""
    phone = Smartphone("Samsung", "Флагман", 100000.0, 5, 95.5, "S23", 256, "Чёрный")
    assert phone.name == "Samsung"
    assert phone.efficiency == 95.5
    assert phone.model == "S23"
    assert phone.memory == 256
    assert phone.color == "Чёрный"


def test_lawn_grass_init():
    """Тест инициализации газонной травы."""
    grass = LawnGrass("Трава", "Элитная", 500.0, 20, "Россия", "7 дней", "Зелёный")
    assert grass.name == "Трава"
    assert grass.country == "Россия"
    assert grass.germination_period == "7 дней"
    assert grass.color == "Зелёный"


def test_add_different_types():
    """Тест сложения разных типов — TypeError."""
    phone = Smartphone("Samsung", "Флагман", 100000.0, 5, 95.5, "S23", 256, "Чёрный")
    grass = LawnGrass("Трава", "Элитная", 500.0, 20, "Россия", "7 дней", "Зелёный")
    with pytest.raises(TypeError):
        phone + grass


def test_add_product_invalid_type(category):
    """Тест добавления не-продукта — TypeError."""
    with pytest.raises(TypeError):
        category.add_product("Not a product")


def test_base_product_is_abstract():
    """Тест, что BaseProduct нельзя создать напрямую."""
    with pytest.raises(TypeError):
        BaseProduct("Товар", "Описание", 100.0, 5)  # type: ignore


def test_creation_logger_mixin(capsys):
    """Тест миксина логирования создания."""
    Product("Тест", "Описание", 100.0, 5)
    captured = capsys.readouterr()
    assert "Создан объект Product" in captured.out
    assert "Тест" in captured.out
