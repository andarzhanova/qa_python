import pytest
from main import BooksCollector

@pytest.fixture(scope="class")
def collector():
    collector = BooksCollector()
    books = ['Гарри Поттер', 'Оно', 'Шерлок Холмс', 'Маугли', 'Недоросль']
    genres = ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
    for i in range(0, len(books)):
        collector.add_new_book(books[i])
        collector.set_book_genre(books[i], genres[i])
    return collector
