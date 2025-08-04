from main import BooksCollector

@pytest.fixture
def collector():
    return BooksCollector()

class TestBooksCollector:

    @pytest.mark.parametrize("book_name, expected_result",
        [
            ["Лангольеры", True],
            ["Book" * 10, True],
            ["B" * 41, False],
            ["", False],
        ])

    def test_add_new_book_add_max_symbol(self, collector, book_name, expected_result):

        collector.add_new_book()
        assert book_name in collector.books_genre == expected_result

    def test_add_book_twice_add_one(self, collector):

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

    def test_set_book_genre_add_true_genge(self, collector, book_name, genre, expected_genre):

        collector.add_new_book()
        
        self.collector.set_book_genre(book_name, genre)
        assert self.collector.get_book_genre(book_name) == expected_genre

    def test_get_books_with_specific_genre_fantasy_will_be_fantasy(self, collector):

        collector.add_new_book()
        self.collector.add_new_book('Тёмный эльф')
        self.collector.add_new_book('Эрагон')
        self.collector.set_book_genre('Тёмный эльф', 'Фэнтази')
        self.collector.set_book_genre('Эрагон', 'Фэнтази')

        result = self.collector.get_books_with_specific_genre('Фэнтази')
        assert result == ['Тёмный эльф', 'Эрагон']

    def test_get_books_genre_empty_books_genre_empty_dict(self, collector):

        collector.add_new_book()
        result = self.collector.get_books_genre()
        assert result == {}

    def test_get_books_genre_single_book_in_genre_one_book_in_dict(self, collector):

        collector.add_new_book()
        book_name = 'Book'
        genre = 'Fantasy'
        self.collector.add_new_book(book_name)
        self.collector.set_book_genre(book_name, genre)

        expected = {book_name: genre}
        result = self.collector.get_books_genre()
        assert result == expected

    def test_get_books_genre_returns_all_books_with_genres(self, collector):

        collector.add_new_book('Книга 1')
        collector.set_book_genre('Книга 1', 'Фантастика')
        collector.add_new_book('Книга 2')
    
        expected = {
        'Книга 1': 'Фантастика',
        'Книга 2': ''
    }
        assert collector.get_books_genre() == expected

    def test_get_books_for_children_book_child(self, collector):

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

    def test_add_book_in_favorites_new_book_once(self, collector, book_name, expected_result):

        collector.add_new_book()
        self.collector.add_new_book(book_name)
        self.collector.add_book_in_favorites(book_name)

        assert (book_name in self.collector.favorites) == expected_result

    def test_delete_book_from_favorites_no_book_from_del(self, collector):

        collector.add_new_book()
        self.collector.add_new_book("Книга для удаления")
        self.collector.add_book_in_favorites("Книга для удаления")

        self.collector.delete_book_from_favorites("Книга для удаления")
        assert "Книга для удаления" not in self.collector.favorites

    def test_get_list_of_favorites_books_single_book_in_favor(self, collector):

        collector.add_new_book()
        self.collector.add_new_book('Избранное')
        self.collector.add_book_in_favorites('Избранное')

        result = self.collector.get_list_of_favorites_books()
        assert result == ['Избранное']
        