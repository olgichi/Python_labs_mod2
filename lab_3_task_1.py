class Book:
    """ Базовый класс книги """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, new_pages: int):
        if not isinstance(new_pages, int):
            raise TypeError("Количество страниц должно быть типа int")

        if new_pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")

        self._pages = new_pages

    def __str__(self):
        return f"Бумажная книга {self.name!r}. Автор {self.author}. Количество страниц {self.pages}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages})"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, new_duration: float):
        if not isinstance(new_duration, float):
            raise TypeError("Продолжительность аудиокниги должна быть типа float ")

        if new_duration <= 0:
            raise ValueError("Продолжительность аудиокниги должна быть неотрицательным числом")

        self._duration = new_duration

    def __str__(self):
        return f"Аудиокнига {self.name!r}. Автор {self.author}. Продолжительность {self.duration}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration})"


book = Book("Жизнь взаймы, или У неба любимчиков нет" , "Э.М.Ремарк")
paper_book = PaperBook("Жизнь взаймы, или У неба любимчиков нет", "Э.М.Ремарк", 384)
audio_book = AudioBook("Жизнь взаймы, или У неба любимчиков нет", "Э.М.Ремарк", 7.4)

print(book.author)
print(book.name)

print(paper_book)
print(repr(paper_book))

print(audio_book.duration)

paper_book.pages = 511
print(paper_book.pages)
