"""Модуль с моделями для e-commerce."""

from abc import ABC, abstractmethod


class CreationLoggerMixin:
    """Миксин для логирования создания объекта."""

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Логирует создание объекта и вызывает родительский конструктор."""
        print(f"Создан объект {self.__class__.__name__} " f"с параметрами: {args}, {kwargs}")
        super().__init__(*args, **kwargs)


class BaseProduct(ABC):
    """Абстрактный базовый класс для всех продуктов."""

    name: str
    description: str
    quantity: int

    @abstractmethod
    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        """Абстрактный конструктор."""
        self.name = name
        self.description = description
        self.quantity = quantity

    @property
    @abstractmethod
    def price(self) -> float:
        """Абстрактный геттер цены."""
        ...

    @price.setter
    @abstractmethod
    def price(self, new_price: float) -> None:
        """Абстрактный сеттер цены."""
        ...

    @abstractmethod
    def __str__(self) -> str:
        """Абстрактное строковое представление."""
        ...

    @abstractmethod
    def __add__(self, other: "BaseProduct") -> float:
        """Абстрактное сложение."""
        ...


class Product(CreationLoggerMixin, BaseProduct):
    """Класс для представления продукта."""

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        """Инициализация продукта."""
        super().__init__(name, description, price, quantity)
        self.__price = price

    @property
    def price(self) -> float:
        """Геттер для цены."""
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        """Сеттер для цены с проверкой."""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        self.__price = new_price

    def __str__(self) -> str:
        """Строковое отображение продукта."""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: "BaseProduct") -> float:
        """Сложение продуктов."""
        if type(self) is not type(other):
            raise TypeError("Складывать можно только одинаковые классы продуктов")
        return self.price * self.quantity + other.price * other.quantity

    @classmethod
    def new_product(cls, product_data: dict) -> "Product":
        """Класс-метод для создания продукта из словаря."""
        return cls(
            name=product_data["name"],
            description=product_data["description"],
            price=product_data["price"],
            quantity=product_data["quantity"],
        )


class Smartphone(Product):
    """Класс для представления смартфона."""

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
        """Инициализация смартфона."""
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    """Класс для представления газонной травы."""

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
        """Инициализация газонной травы."""
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color


class Category:
    """Класс для представления категории."""

    name: str
    description: str

    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, products: list[Product]) -> None:
        """Инициализация категории."""
        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.product_count += len(products)

    def __str__(self) -> str:
        """Строковое отображение категории."""
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def add_product(self, product: Product) -> None:
        """Добавляет продукт в категорию с проверкой типа."""
        if not issubclass(type(product), BaseProduct):
            raise TypeError("Можно добавлять только продукты или их наследников")
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        """Геттер для списка товаров."""
        return "".join(f"{product}\n" for product in self.__products)
