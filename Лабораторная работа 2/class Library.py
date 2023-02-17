from typing import Optional

BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


# TODO написать класс Book
class Book:
    def __init__(self, id_: int, name: int, pages: int):
        self.id = id_
        self.name = name
        self.pages = pages

# TODO написать класс Library
class Library():
    def __init__(books: dict):
        books: Optional[str]

    def get_next_book_id(id_:Book) -> int:
        if Book == None:
            return 1
        if Book != None:
            last_book = self.books[-1]
            next_id = last_book['id'] + 1
            return next_id

    def get_index_by_book_id(id_:Book):
        if id_ != None:
            return id
        if id_== None:
            raise ValueError("Книги с запрашиваемым id не существует")


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
