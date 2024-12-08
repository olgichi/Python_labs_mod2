# TODO: Подробно описать три произвольных класса
import doctest

# TODO: описать класс



class Hogwarts:
    def __init__(self, house: str, number_of_students: int):
        """
        Создание объекта "Хогвартс"

        :param house: Название факультета (Gryffindor, Slytherin, Hufflepuff и Ravenclaw)
        :param number_of_students: Количество студентов на факультете (положительное число)

        Примеры:
        >>> hogwarts = Hogwarts('Gryffindor', 50)
        """
        allowed_houses = {'Gryffindor', 'Slytherin', 'Hufflepuff', 'Ravenclaw'}
        if not isinstance(house, str):
            raise TypeError("Название факультета должно быть строкой")
        if not house or house not in allowed_houses:
            raise ValueError("Название факультета должно быть одним из: Gryffindor, Slytherin, Hufflepuff, Ravenclaw")
        self.house = house

        if not isinstance(number_of_students, int):
            raise TypeError("Количество студентов должно быть целым числом")
        if number_of_students <= 0:
            raise ValueError("Количество студентов должно быть положительным целым числом")
        self.number_of_students = number_of_students

    def add_students(self, count: int) -> None:
        """
        Добавление студентов на факультет

        :param count: Количество добавляемых студентов (положительное)
        :raise TypeError: Если число не int
        :raise ValueError: Если число отрицательное

        Примеры:
        >>> hogwarts = Hogwarts('Gryffindor', 50)
        >>> hogwarts.add_students(10)
        >>> hogwarts.number_of_students
        60
        """
        if not isinstance(count, int):
            raise TypeError("Количество добавляемых студентов должно быть целым числом")
        if count <= 0:
            raise ValueError("Количество добавляемых студентов должно быть положительным целым числом")
        self.number_of_students += count

    def change_house(self, new_house: str) -> None:
        """
        Изменение факультета студента

        :param new_house: Новое название факультета
        :raise TypeError: Если факультет - не строка
        :raise ValueError: Если новое название факультета некорректно
        """
        if not isinstance(new_house, str):
            raise TypeError("Новое название факультета должно быть строкой")
        allowed_houses = {'Gryffindor', 'Slytherin', 'Hufflepuff', 'Ravenclaw'}
        if not new_house or new_house not in allowed_houses:
            raise ValueError(
                "Новое название факультета должно быть одним из: Gryffindor, Slytherin, Hufflepuff, Ravenclaw")
        self.house = new_house

    def get_house_info(self) -> str:
        """
        Получение информации о факультете

        :return: Строка с информацией о факультете и количестве студентов.

        Примеры:
        >>> hogwarts = Hogwarts('Gryffindor', 50)
        >>> hogwarts.get_house_info()
        'House: Gryffindor, Students: 50'
        """
        return f"House: {self.house}, Students: {self.number_of_students}"

# TODO: описать ещё класс

class Dragon:
    def __init__(self, species: str, origin_country: str, age: int, is_flying: bool):
        """
        Создание объекта "Дракон"

        :param species: Вид дракона (например, Fire, Ice)
        :param origin_country: Страна происхождения дракона (например, China, Scotland)
        :param age: Возраст дракона в годах (положительное число)
        :param is_flying: Флаг, указывающий, летит ли дракон (True или False)

        Примеры:
        >>> dragon = Dragon('Fire', 'China', 5, True)
        """
        if not isinstance(species, str):
            raise TypeError("Вид дракона должен быть строкой")
        if not species:
            raise ValueError("Вид дракона должен быть непустой строкой")
        self.species = species

        if not isinstance(origin_country, str):
            raise TypeError("Страна происхождения должна быть строкой")
        if not origin_country:
            raise ValueError("Страна происхождения должна быть непустой строкой")
        self.origin_country = origin_country

        if not isinstance(age, int):
            raise TypeError("Возраст дракона должен быть целым числом")
        if age <= 0:
            raise ValueError("Возраст дракона должен быть положительным целым числом")
        self.age = age

        if not isinstance(is_flying, bool):
            raise TypeError("Флаг 'летит' должен быть логическим значением (True или False)")
        self.is_flying = is_flying

    def grow(self, years: int) -> None:
        """
        Увеличение возраста дракона

        :param years: Количество лет, на которое следует увеличить возраст (положительное число)
        :raise TypeError: Если число лет - не int
        :raise ValueError: Если число отрицательное

        Примеры:
        >>> dragon = Dragon('Fire', 'China', 5, True)
        >>> dragon.grow(3)
        >>> dragon.age
        8
        """
        if not isinstance(years, int):
            raise TypeError("Количество лет должно быть целым числом")
        if years <= 0:
            raise ValueError("Количество лет должно быть положительным целым числом")
        self.age += years

    def fly(self) -> str:
        """
        Проверка, летит ли дракон

        :return: Строка с сообщением о том, летит ли дракон

        Примеры:
        >>> dragon = Dragon('Fire', 'China', 5, True)
        >>> dragon.fly()
        'The Fire dragon is flying!'
        """
        return f"The {self.species} dragon is {'flying!' if self.is_flying else 'not flying.'}"
# TODO: и ещё один

class MagicWand:
    def __init__(self, length: float, material: str):
        """
        Создание объекта "Волшебная палочка"

        :param length: Длина волшебной палочки (дюймы) (положительное число)
        :param material: Сердцевина волшебной палочки (например, unicorn hair,
        dragon heartstring, phoenix feather)

        Примеры:
        >>> wand = MagicWand(10.5, 'phoenix feather')
        """
        if not isinstance(length, (int, float)):
            raise TypeError("Длина волшебной палочки должна быть числом (int или float)")
        if length <= 0:
            raise ValueError("Длина волшебной палочки должна быть положительным числом")
        self.length = length

        if not isinstance(material, str):
            raise TypeError("Сердцевина волшебной палочки должна быть строкой")
        if not material:
            raise ValueError("Сердцевина волшебной палочки должна быть непустой строкой")
        self.material = material

    def cast_spell(self, spell: str = "Lumos") -> str:
        """
        Произнесение заклинания

        :param spell: Заклинание, которое будет произнесено (по умолчанию "Lumos")
        :raise: TypeErrorr: Если заклиненание - не строка
        :return: Строка с сообщением о заклинании

        Примеры:
        >>> wand = MagicWand(.5, 'phoenix feather')
        >>> wand.cast_spell()
        'Casting spell: Lumos'
        >>> wand.cast_spell('Expelliarmus')
        'Casting spell: Expelliarmus'
        """
        if not isinstance(spell, str):
            raise TypeError("Заклинание должно быть строкой")
        return f"Casting spell: {spell}"

    def get_wand_info(self) -> str:
        """
        Получение информации о волшебной палочке

        :return: Строка с информацией о длине и сердцевине

        Примеры:
        >>> wand = MagicWand(10.5, 'phoenix feather')
        >>> wand.get_wand_info()
        'Wand Length: 10.5 inch, Material: phoenix feather'
        """
        return f"Wand Length: {self.length} inch, Material: {self.material}"

if __name__ == "__main__":
    doctest.testmod()

