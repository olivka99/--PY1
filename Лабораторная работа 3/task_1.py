class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def author(self):
        return self._author

    @prop.setter
    def author(self, new_author: int) -> None:
        if not isinstance(new_author, int):
            raise TypeError("Имя автора должно быть типа int")
        self._author = new_author

    @property
    def name(self):
        return self._name

    @prop.setter
    def name(self, new_name: int) -> None:
        if not isinstance(new_name, int):
            raise TypeError("Название книги должно быть типа int")
        self._name = new_name

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}"

    def __repr__(self) -> str:
        return f'{self.__class__.name__}(name={self._name!r}, author={self._author!r})'


class PaperBook(Book):
    def __init__(self, pages: int):
        super().__init__(name, author)
        self.pages = pages

    @property
    def pages(self) -> int:
        return self._pages

    @pages.setter
    def pages(self, new_pages: int) -> None:
        if not isinstance(new_pages, int):
            raise TypeError("Количество страниц должно быть типа int")
        if new_pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self._pages = new_pages

    def __repr__(self) -> str:
        return f'{self.__class__.name__}(name={self._name!r}, author={self._author!r}, pages={self.pages!r})'


class AudioBook(Book):
    def __init__(self, duration: bool):
        self.duration = duration
        super().__init__(name, author)

    @property
    def duration(self) -> bool:
        return self._duration

    @duration.setter
    def duration(self, new_duration: bool) -> None:
        if not isinstance(new_duration, bool):
            raise TypeError("Продолжительность книги должна быть типа bool")
        if new_duration <= 0:
            raise ValueError("Продолжительность книги должна быть положительным числом")
        self._duration = new_duration

    def __repr__(self) -> str:
        return f'{self.__class__.name__}(name={self._name!r}, author={self._author!r}, duration={self.duration!r})'


