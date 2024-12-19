import pytest


class BooksCollector:

    def __init__(self):
        self.books_genre = {}
        self.favorites = []
        self.genre = ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
        self.genre_age_rating = ['Ужасы', 'Детективы']

    # добавляем новую книгу
    def add_new_book(self, name):
        if not self.books_genre.get(name) and 0 < len(name) < 41:
            self.books_genre[name] = ''

    # устанавливаем книге жанр
    def set_book_genre(self, name, genre):
        if name in self.books_genre and genre in self.genre:
            self.books_genre[name] = genre

    # получаем жанр книги по её имени
    def get_book_genre(self, name):
        return self.books_genre.get(name)

    # выводим список книг с определённым жанром
    def get_books_with_specific_genre(self, genre):
        books_with_specific_genre = []
        if self.books_genre and genre in self.genre:
            for name, book_genre in self.books_genre.items():
                if book_genre == genre:
                    books_with_specific_genre.append(name)
        return books_with_specific_genre

    # получаем словарь books_genre
    def get_books_genre(self):
        return self.books_genre

    # возвращаем книги, подходящие детям
    def get_books_for_children(self):
        books_for_children = []
        for name, genre in self.books_genre.items():
            if genre not in self.genre_age_rating and genre in self.genre:
                books_for_children.append(name)
        return books_for_children

    # добавляем книгу в Избранное
    def add_book_in_favorites(self, name):
        if name in self.books_genre:
            if name not in self.favorites:
                self.favorites.append(name)

    # удаляем книгу из Избранного
    def delete_book_from_favorites(self, name):
        if name in self.favorites:
            self.favorites.remove(name)

    # получаем список Избранных книг
    def get_list_of_favorites_books(self):
        return self.favorites


def test_add_new_book_books_genre_book_in_list():
    book = BooksCollector()
    book_name = 'Книга'
    book.add_new_book(book_name)

    assert book.get_books_genre().get(book_name) == '', f"Книга '{book_name}'  добавлена"


@pytest.mark.parametrize('genre', ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии'])
def test_set_book_genre_with_your_name_passed(genre):
    book = BooksCollector()
    book_name = "Книга"
    book.add_new_book(book_name)
    book.set_book_genre(book_name, genre)

    assert book.get_book_genre(book_name) == genre


def test_get_book_genre_with_your_name_passed():
    book = BooksCollector()
    book.add_new_book("HIMYM")
    book.set_book_genre("HIMYM", "Комедии")
    genre = book.get_book_genre("HIMYM")

    assert genre == "Комедии", f"Ожидаемый результат 'Комедии', получено {genre}"


@pytest.mark.parametrize(
    "genre, expected_books",
    [
        ('Фантастика', ['Book 1']),
        ('Ужасы', ['Book 2']),
        ('Детективы', ['Book 3']),
        ('Мультфильмы', ['Book 4']),
        ('Комедии', ['Book 5'])
    ]
)
def test_get_books_with_specific_genre_passed(genre, expected_books):
    book = BooksCollector()
    book.books_genre = {
        'Book 1': 'Фантастика',
        'Book 2': 'Ужасы',
        'Book 3': 'Детективы',
        'Book 4': 'Мультфильмы',
        'Book 5': 'Комедии'
    }

    result = book.get_books_with_specific_genre(genre)
    assert result == expected_books, f"Ожидалось {expected_books}, получено {result}"


def test_get_books_genre_list_books_passed():
    book = BooksCollector()
    assert book.get_books_genre() == {}, 'Словарь получен'


def test_get_books_for_children_return_for_children():
    book = BooksCollector()
    book.books_genre = {
        'Book 1': 'Фантастика',
        'Book 2': 'Ужасы',
        'Book 3': 'Детективы',
        'Book 4': 'Мультфильмы',
        'Book 5': 'Комедии'
    }
    result = book.get_books_for_children()
    assert result == ['Book 1', 'Book 4', 'Book 5']


def test_add_book_in_favorites_book_in_list():
    book = BooksCollector()
    book.add_new_book('Книга')
    book.add_book_in_favorites('Книга')
    assert 'Книга' in book.get_list_of_favorites_books(), 'Книга должна быть в списке избранного'


def test_delete_book_from_favorites_book_in_list():
    book = BooksCollector()
    book.add_new_book('Книга')
    book.add_book_in_favorites('Книга')
    book.delete_book_from_favorites('Книга')
    assert 'Книга' not in book.get_list_of_favorites_books(), 'Книга удалена из списка избранного'


def test_get_list_of_favorites_books_list_books_passed():
    book = BooksCollector()
    book.add_new_book('Book 1')
    book.add_new_book('Book 2')
    book.add_book_in_favorites('Book 1')
    book.add_book_in_favorites('Book 2')
    assert book.get_list_of_favorites_books() == ['Book 1', 'Book 2'], 'Список избранных книг не совпадает с ожидаемым'
