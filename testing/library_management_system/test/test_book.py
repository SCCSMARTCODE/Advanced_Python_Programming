from unittest import TestCase, main
import os, sys

from testing.library_management_system.app.book import BOOKS_DB, load_books, save_books


class BookFunctionalityTest(TestCase):

    def test_load_book_with_db_not_existing(self):
        result = load_books()
        self.assertEqual(result, [])

    def test_load_book_with_db_existing(self):
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

if __name__ == '__main__':
    main()