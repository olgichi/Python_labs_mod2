import doctest


class Amaryllis:
    """
    Класс описывает цветы семейства амариллисовые
    """
    def __init__(self, name: str, height: float):
        """
        Создание и подготовка к работе объекта "Цветок семейства амариллисовые"
        :param name: Название цветка
        :param height: Высота цветка в сантиметрах
        Примеры:
        >>> flower = Amaryllis("Амариллис", 50.0)
        """
        self._name = name  # Наследуем атрибуты name и height
        self.height = height  # Инициализируем публичный атрибут, отработает setter свойства

    @property
    def name(self) -> str:
        """Возвращает название цветка """
        return self._name

    @property
    def height(self) -> float:
        """Возвращает высоту цветка"""
        return self._height

    @height.setter
    def height(self, new_height: float) -> None:
        """Устанавливает новую высоту цветка"""
        if not isinstance(new_height, (int, float)):
            raise TypeError("Высота цветка должна быть числом типа int или float")
        if new_height <= 0:
            raise ValueError("Высота цветка должна быть положительным числом")
        self._height = new_height

    def __str__(self) -> str:
        """Метод для чтения"""
        return f"Название цветка: {self.name}. Высота: {self.height} см."

    def __repr__(self) -> str:
        """Возвращает строку,  показывающую, как может быть инициализирован экземпляр"""
        return f"{self.__class__.__name__}(name={self.name!r}, height={self.height})"

    def fragrance(self) -> str:
        """Метод, который возвращает описание аромата цветка """
        return "Ароматный"


class Narcissus(Amaryllis):
    """Класс, который описывает нарциссы (цветы семейства амариллисовые)"""
    def __init__(self, name: str, height: float, color: str):
        """
        Создание и подготовка к работе объекта "Нарцисс",
        дочерний класс объекта "Цветок семейства амариллисовые"
        :param name: Название цветка
        :param height: Высота цветка в сантиметрах
        :param color: Цвет нарцисса
        Примеры:
        >>> flower_1 = Narcissus("Нарцисс", 30.0, "Желтый")
        """
        super().__init__(name, height)  # Инициализируем защищенный атрибут
        self._color = color  # Инициализируем защищенный атрибут

    @property
    def color(self) -> str:
        """Возвращает цвет нарцисса"""
        return self._color

    def __str__(self) -> str:
        """Метод для чтения """
        return f"Название цветка: {self.name}. Высота: {self.height} см. Цвет: {self.color}."

    def __repr__(self) -> str:
        """Возвращает строку, показывающую, как может быть инициализирован экземпляр  """
        return f"{self.__class__.__name__}(name={self.name!r}, height={self.height}, color={self.color!r})"

    def fragrance(self) -> str:
        """Перегрузка метода, чтобы он возвращал описание аромата для нарциссов """
        return "Сладкий аромат"


if __name__ == "__main__":
    doctest.testmod()
    pass
