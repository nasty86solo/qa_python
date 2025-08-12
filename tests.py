from main import BooksCollector
import pytest

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

        collector.add_new_book(book_name)
        assert (book_name in collector.books_genre) == expected_result

    def test_add_book_twice_add_one(self, collector):

        book_name = 'Сияющий'
        collector.add_new_book(book_name)
        collector.add_new_book(book_name)
        
        assert len(collector.books_genre) == 1
        assert book_name in collector.books_genre

    @pytest.mark.parametrize("book_name, genre, expected_genre",
        [
            ['Тёмный эльф', 'Фантастика', 'Фантастика'],
            ['Я убиваю', 'Детективы', 'Детективы'],
        ])

    def test_set_book_genre_add_true_genge(self, collector, book_name, genre, expected_genre):

        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.get_book_genre(book_name) == expected_genre

    def test_get_book_genre_existing_book(self, collector):
        
        book_name = 'Собака Баскервилей'
        genre = 'Ужасы'
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.get_book_genre(book_name) == genre
        
    def test_get_books_with_specific_genre_fantasy_will_be_fantasy(self, collector):

        collector.add_new_book('Тёмный эльф')
        collector.add_new_book('Эрагон')
        collector.set_book_genre('Тёмный эльф', 'Фантастика')
        collector.set_book_genre('Эрагон', 'Фантастика')

        result = collector.get_books_with_specific_genre('Фантастика')
        assert result == ['Тёмный эльф', 'Эрагон']

    def test_get_books_genre_empty_on_new_books(self, collector):

        collector.add_new_book('Книга')
    
        result = collector.get_books_genre()
        assert result == {'Книга': ''}

    def test_get_books_genre_single_book_in_genre_one_book_in_dict(self, collector):

        book_name = 'Book'
        genre = 'Фантастика'
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)

        expected = {book_name: genre}
        result = collector.get_books_genre()
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

        collector.add_new_book('Мультфильм')
        collector.add_new_book('Комедия')
        collector.add_new_book('Детектив')

        collector.set_book_genre('Мультфильм', 'Мультфильмы')
        collector.set_book_genre('Комедия', 'Комедии')
        collector.set_book_genre('Детектив', 'Детективы')

        result = collector.get_books_for_children()
        assert result == ['Мультфильм', 'Комедия']
      
    @pytest.mark.parametrize("book_name, expected_result", 
        [
            ["Избранная книга", True],
            ["Недобавленная книга", False]
        ])
    def test_add_book_in_favorites_new_book_once(self, collector, book_name, expected_result):
    
        if expected_result:
            collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        assert (book_name in collector.favorites) == expected_result

    def test_add_book_in_favorites_twice(self, collector):
    
        book_name = "Уже в избранном"
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        assert book_name in collector.favorites
    
        collector.add_book_in_favorites(book_name)
        assert len(collector.favorites) == 1
        assert book_name in collector.favorites

    def test_add_nonexistent_book_to_favorites(self, collector):
    
        book_name = "Несуществующая книга"
        collector.add_book_in_favorites(book_name)
        assert book_name not in collector.favorites

    def test_delete_book_from_favorites_no_book_from_del(self, collector):

        collector.add_new_book("Книга для удаления")
        collector.add_book_in_favorites("Книга для удаления")

        collector.delete_book_from_favorites("Книга для удаления")
        assert "Книга для удаления" not in collector.favorites

    def test_get_list_of_favorites_books_single_book_in_favor(self, collector):

        collector.add_new_book('Избранное')
        collector.add_book_in_favorites('Избранное')

        result = collector.get_list_of_favorites_books()
        assert result == ['Избранное']
        