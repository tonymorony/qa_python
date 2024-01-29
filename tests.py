from main import BooksCollector

import pytest
# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        assert len(collector.books_genre) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    def test_add_new_book_same_name_twice_adding_one(self):
        collector = BooksCollector()

        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert len(collector.get_books_genre()) == 1

    def test_add_new_book_name_length_more_than_max_not_adding(self):
        collector = BooksCollector()

        # имя длиной 43 символа
        collector.add_new_book('Что делать, если ваш кот хочет вас убить!!!')

        assert len(collector.get_books_genre()) == 0

    @pytest.mark.parametrize('genre', ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии'])
    def test_set_book_genre_existing_genre_one_book(self, genre):
        collector = BooksCollector()

        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', genre)

        assert collector.get_book_genre('Что делать, если ваш кот хочет вас убить') == genre

    def test_set_book_genre_not_existing_genre_empty(self):
        collector = BooksCollector()

        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Энциклопедия')

        assert collector.get_book_genre('Что делать, если ваш кот хочет вас убить') == ''

    def test_get_book_genre_not_existing_name_none(self):
        collector = BooksCollector()

        assert collector.get_book_genre('Такой книги нет') is None

    def test_get_books_with_specific_genre_existing_genre_one_book(self):
        collector = BooksCollector()

        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Детективы')

        assert len(collector.get_books_with_specific_genre('Детективы')) == 1

    def test_get_books_genre_no_books_added_empty(self):
        collector = BooksCollector()

        assert len(collector.get_books_genre()) == 0

    @pytest.mark.parametrize('genre', ['Фантастика', 'Мультфильмы', 'Комедии'])
    def test_get_books_for_children_one_book__suitable_genre_returning(self, genre):
        collector = BooksCollector()

        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', genre)

        assert len(collector.get_books_for_children()) == 1

    @pytest.mark.parametrize('genre', ['Ужасы', 'Детективы'])
    def test_get_books_for_children_one_book_not_suitable_genre_empty(self, genre):
        collector = BooksCollector()

        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', genre)

        assert collector.get_books_for_children() == []

    def test_add_book_to_favorites_one_book(self):
        collector = BooksCollector()

        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Детективы')

        collector.add_book_to_favorites('Что делать, если ваш кот хочет вас убить')

        assert len(collector.get_list_of_favorites_books()) == 1

    def test_delete_book_from_favorites_one_book(self):
        collector = BooksCollector()

        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Детективы')
        collector.add_book_to_favorites('Что делать, если ваш кот хочет вас убить')

        collector.delete_book_from_favorites('Что делать, если ваш кот хочет вас убить')

        assert len(collector.get_list_of_favorites_books()) == 0

    def test_get_list_of_favorites_books_no_books_added_empty(self):
        collector = BooksCollector()

        assert len(collector.get_list_of_favorites_books()) == 0
