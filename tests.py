from main import BooksCollector


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    #test 1 Проверка добавления книг.
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    #test 2 Нельзя добавить одну и ту же книгу дважды.
    def test_add_two_new_same_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()
        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Гордость и предубеждение и зомби')
        assert len(collector.get_books_rating()) != 2

    #test3 нельзя выставить рейтинг книге, которой нет в списке.
    def test_not_paste_rating_not_existent_book(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()
        collector.set_book_rating('Волк и Лиса', 2)
        assert collector.get_book_rating('Волк и Лиса') == None

    #test4 Нельзя выставить рейтинг меньше 1.
    def test_not_paste_rating_less_than_one(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_rating('Гордость и предубеждение и зомби', -1)
        assert collector.get_book_rating('Гордость и предубеждение и зомби') != -1

    #test5 Нельзя выставить рейтинг больше 10.
    def test_not_paste_rating_more_ten(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_rating('Гордость и предубеждение и зомби', 11)
        assert collector.get_book_rating('Гордость и предубеждение и зомби') != 11

    #test6 У не добавленной книги нет рейтинга.
    def test_not_add_book_not_rating(self):
        collector = BooksCollector()
        assert collector.get_book_rating('Собака друг человека') == None

    #test7 Добавление книги в избранное.
    def test_add_book_favorite_list(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        assert 'Гордость и предубеждение и зомби' in collector.get_list_of_favorites_books()

    #test8 Нельзя добавить книгу в избранное, если её нет в словаре
    def test_not_add_book_favorit_list_if_your_not_in_books(self):
        collector = BooksCollector()
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        assert 'Гордость и предубеждение и зомби'not in collector.get_list_of_favorites_books()

    #test9 Проверка удаления книги из избранного.
    def test_dellete_book_favorits_list(self):
        collector = BooksCollector()
        collector.add_new_book('Котишки')
        collector.add_book_in_favorites('Котишки')
        collector.delete_book_from_favorites('Котишки')
        assert 'Котишки' not in collector.get_list_of_favorites_books()
