import pytest
from main import BooksCollector

class TestBooksCollector:

    def test_add_new_book_add_five_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        collector.add_new_book('Оно')
        collector.add_new_book('Шерлок Холмс')
        collector.add_new_book('Маугли')
        collector.add_new_book('Недоросль')
        assert len(collector.get_books_genre()) == 5

    def test_set_book_genre_set_book_genre_from_list_with_genres(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')
        assert collector.get_book_genre('Гарри Поттер') in collector.genre

    @pytest.mark.parametrize(
        'name, genre',
        [
            ['Гарри Поттер', 'Фантастика'],
            ['Оно', 'Ужасы'],
            ['Шерлок Холмс', 'Детективы'],
            ['Маугли', 'Мультфильмы'],
            ['Недоросль', 'Комедии']
        ]
    )
    def test_get_book_genre_get_book_genre_by_name(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_book_genre(name) == genre

    def test_get_books_with_specific_genre_get_books_with_fantasy_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        collector.add_new_book('Дюна')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')
        collector.set_book_genre('Дюна', 'Фантастика')
        assert collector.get_books_with_specific_genre('Фантастика') == ['Гарри Поттер', 'Дюна']

    def test_get_books_genre_get_dictionary_with_added_books_genres(self):
        collector = BooksCollector()
        collector.add_new_book('Оно')
        collector.add_new_book('Шерлок Холмс')
        collector.set_book_genre('Оно', 'Ужасы')
        collector.set_book_genre('Шерлок Холмс', 'Детективы')
        assert collector.get_books_genre() == {'Оно': 'Ужасы', 'Шерлок Холмс': 'Детективы'}

    @pytest.mark.parametrize('name', ['Оно', 'Шерлок Холмс'])
    def test_get_books_for_children_no_books_with_genre_age_rating(self, name):
        collector = BooksCollector()
        collector.add_new_book('name')
        collector.set_book_genre('name', 'Ужасы')
        collector.set_book_genre('name', 'Детективы')
        assert name not in (collector.get_books_for_children())

    def test_add_book_in_favorites_add_two_books_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        collector.add_new_book('Оно')
        collector.add_book_in_favorites('Гарри Поттер')
        collector.add_book_in_favorites('Оно')
        assert len(collector.get_list_of_favorites_books()) == 2

    def test_delete_book_from_favorites_delete_harry_potter_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        collector.add_new_book('Оно')
        collector.add_book_in_favorites('Гарри Поттер')
        collector.add_book_in_favorites('Оно')
        collector.delete_book_from_favorites('Гарри Поттер')
        assert 'Гарри Поттер' not in collector.get_list_of_favorites_books()

    def test_get_list_of_favorites_books_get_list_with_added_books(self):
        collector = BooksCollector()
        collector.add_new_book('Шерлок Холмс')
        collector.add_new_book('Маугли')
        collector.add_book_in_favorites('Шерлок Холмс')
        collector.add_book_in_favorites('Маугли')
        assert collector.get_list_of_favorites_books() == ['Шерлок Холмс', 'Маугли']
