import builtins
from unittest import TestCase, main, mock
import os, sys

from testing.library_management_system.app.book import BOOKS_DB, load_books, save_books, add_book, remove_book, \
    update_book, borrow_book, datetime
from testing.library_management_system.app.user import UserObj


class BookFunctionalityTest(TestCase):

    def setUp(self):
        pass

    def test_load_book_with_db_not_existing(self):
        if os.path.exists(BOOKS_DB):
            os.remove(BOOKS_DB)
        result = load_books()
        self.assertEqual(result, [])

    def test_load_books_and_save_books_with_db_existing(self):
        books = [
            {
                "title": "title",
                "author": "author",
                "genre": "genre",
                "available_copies": 10,
                "borrowed_copies": 0,
                "transactions": []
            }
        ]
        save_books(books)
        result = load_books()
        self.assertEqual(result, books)
        os.remove(BOOKS_DB)

    def test_add_book(self):
        books = [
            {
                "title": "title",
                "author": "author",
                "genre": "genre",
                "available_copies": 10,
                "borrowed_copies": 0,
                "transactions": []
            },
            {
                "title": "title1",
                "author": "author1",
                "genre": "genre",
                "available_copies": 20,
                "borrowed_copies": 0,
                "transactions": []
            }
        ]
        save_books([books[0]])
        with mock.patch('builtins.input') as patch_input:
            patch_input.side_effect = [
                                        books[1]['title'],
                                        books[1]['author'],
                                        books[1]['genre'],
                                        books[1]['available_copies']
                                    ]
            add_book()
        result = load_books()

        self.assertEqual(result, books)
        os.remove(BOOKS_DB)


    def test_remove_book(self):
        books = [
            {
                "title": "title",
                "author": "author",
                "genre": "genre",
                "available_copies": 10,
                "borrowed_copies": 0,
                "transactions": []
            },
            {
                "title": "title1",
                "author": "author1",
                "genre": "genre",
                "available_copies": 20,
                "borrowed_copies": 0,
                "transactions": []
            }
        ]
        save_books(books)
        with mock.patch('builtins.input') as patch_input:
            patch_input.return_value = books[1]['title']
            remove_book()
        result = load_books()
        self.assertEqual(result, [books[0]])
        os.remove(BOOKS_DB)

    def test_update_book(self):
        books = [
            {
                "title": "title",
                "author": "author",
                "genre": "genre",
                "available_copies": 10,
                "borrowed_copies": 0,
                "transactions": []
            },
            {
                "title": "title1",
                "author": "author1",
                "genre": "genre",
                "available_copies": 20,
                "borrowed_copies": 0,
                "transactions": []
            }
        ]

        book1_updated_version = {
                "title": "title1",
                "author": "author1_updated",
                "genre": "genre_updated",
                "available_copies": 10,
                "borrowed_copies": 0,
                "transactions": []
            }
        save_books(books)
        with mock.patch('builtins.input') as patch_input:
            patch_input.side_effect = [
                                        book1_updated_version['title'],
                                        book1_updated_version['author'],
                                        book1_updated_version['genre'],
                                        book1_updated_version['available_copies']
                                    ]
            update_book()
        result = load_books()
        self.assertEqual(result[1], book1_updated_version)
        os.remove(BOOKS_DB)

    def test_borrow_book(self):
        books = [
            {
                "title": "title",
                "author": "author",
                "genre": "genre",
                "available_copies": 10,
                "borrowed_copies": 0,
                "transactions": []
            },
            {
                "title": "title1",
                "author": "author1",
                "genre": "genre",
                "available_copies": 20,
                "borrowed_copies": 0,
                "transactions": []
            }
        ]
        save_books(books)
        with mock.patch('builtins.input') as patch_input:
            user = UserObj(username="test", email="test@gmail.com", mode="client")
            patch_input.return_value = books[0]['title']
            patch_date_return_value = datetime.now()
            with mock.patch('datetime') as patch_date:
                patch_date.now.return_value = lambda :patch_date_return_value
                borrow_book(user)
        result = load_books()
        self.assertTrue(result[0]['transactions'])
        self.assertEqual(result[0]['transactions'].get("email"), user.email)
        self.assertEqual(result[0]['available_copies'], books[0]['available_copies'] - 1)
        self.assertEqual(result[0]['borrowed_copies'], 1)
        os.remove(BOOKS_DB)


if __name__ == '__main__':
    main()