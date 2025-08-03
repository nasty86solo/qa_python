from main import BooksCollector

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
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    @pytest.mark.parametrize("book_name, expected_result",
        [
            ["Лангольеры", True],
            ["Book" * 10, True],
            ["B" * 41, False],
            ["", False],
        ])

    def test_add_new_book_add_max_symbol(self, book_name, expected_result):

        collector = BooksCollector()
        collector.add_new_book('Лангольеры')
        collector.add_new_book('Book' * 10)
        collector.add_new_book('B' * 41)
        collector.add_new_book('')

        self.collector.add_new_book(book_name)
        assert book_name in self.collector.books_genre == expected_result

    def test_add_book_twice_add_one(self):

        collector = BooksCollector()
        collector.add_new_book(book_name)
        book_name = 'Сияющий'

        self.collector.add_new_book(book_name)
        assert book_name in self.collector.books_genre

        self.collector.add_new_book(book_name)
        assert len(self.collector.books_genre) == 1
        assert book_name in self.collector.books_genre

    @pytest.mark.parametrize("book_name, genre, expected_genre",
        [
            ['Тёмный эльф', 'Фэнтази', 'Фэнтази'],
            ['Я убиваю', 'Триллер', 'Триллер'],
        ])

    def test_set_book_genre_add_true_genge(self, book_name, genre, expected_genre):

        collector = BooksCollector()
        collector.add_new_book('Тёмный эльф')
        collector.add_new_book('Я убиваю')

        self.collector.set_book_genre(book_name, genre)
        assert self.collector.get_book_genre(book_name) == expected_genre

    def test_get_books_with_specific_genre_fantasy_will_be_fantasy(self):

        collector = BooksCollector()
        collector.add_new_book()
        self.collector.add_new_book('Тёмный эльф')
        self.collector.add_new_book('Эрагон')
        self.collector.set_book_genre('Тёмный эльф', 'Фэнтази')
        self.collector.set_book_genre('Эрагон', 'Фэнтази')

        result = self.collector.get_books_with_specific_genre('Фэнтази')
        assert result == ['Тёмный эльф', 'Эрагон']

    def test_get_books_genre_empty_books_genre_empty_dict(self):

        collector = BooksCollector()
        collector.add_new_book()
        result = self.collector.get_books_genre()
        assert result == {}

    def test_get_books_genre_single_book_in_genre_one_book_in_dict(self):

        collector = BooksCollector()
        collector.add_new_book()
        book_name = 'Book'
        genre = 'Fantasy'
        self.collector.add_new_book(book_name)
        self.collector.set_book_genre(book_name, genre)

        expected = {book_name: genre}
        result = self.collector.get_books_genre()
        assert result == expected

    def test_get_books_for_children_book_child(self):

        collector = BooksCollector()
        collector.add_new_book()
        self.collector.add_new_book('Мультфильм')
        self.collector.add_new_book('Комедия')
        self.collector.add_new_book('Детектив')

        self.collector.set_book_genre('Мультфильм', 'Мультфильмы')
        self.collector.set_book_genre('Комедия', 'Комедии')
        self.collector.set_book_genre('Детектив', 'Детективы')

        result = self.collector.get_books_for_children()
        assert result == ['Мультфильм', 'Комедия']

    @pytest.mark.parametrize("book_name, expected_result",
        [
            ("Избранная книга", True),
            ("Уже в избранном", False),
            ("Недобавленная книга", False)
        ])

    def test_add_book_in_favorites_new_book_once(self, book_name, expected_result):

        collector = BooksCollector()
        collector.add_new_book()
        self.collector.add_new_book(book_name)
        self.collector.add_book_in_favorites(book_name)

        assert (book_name in self.collector.favorites) == expected_result

    def test_delete_book_from_favorites_no_book_from_del(self):

        collector = BooksCollector()
        collector.add_new_book()
        self.collector.add_new_book("Книга для удаления")
        self.collector.add_book_in_favorites("Книга для удаления")

        self.collector.delete_book_from_favorites("Книга для удаления")
        assert "Книга для удаления" not in self.collector.favorites

    def test_get_list_of_favorites_books_single_book_in_favor(self):

        collector = BooksCollector()
        collector.add_new_book()
        self.collector.add_new_book('Избранное')
        self.collector.add_book_in_favorites('Избранное')

        result = self.collector.get_list_of_favorites_books()
        assert result == ['Избранное']
        
