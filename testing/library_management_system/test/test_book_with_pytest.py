import pytest
import os
from testing.library_management_system.app.book import BOOKS_DB, load_books, save_books, add_book, remove_book, \
    update_book, borrow_book, datetime, return_book


class TestBookFunctionality:

    @staticmethod
    @pytest.fixture(scope='class')
    def books():
        return [
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

    @staticmethod
    def test_load_book_with_db_not_existing():
        if os.path.exists(BOOKS_DB):
            os.remove(BOOKS_DB)
        result = load_books()
        assert result == []

    @staticmethod
    def test_load_books_and_save_books_with_db_existing(books):
        save_books(books)
        result = load_books()
        assert result == books
        os.remove(BOOKS_DB)


if __name__ == "__main__":
    pytest_args = ["-q", "--tb=short", "."]

    pytest.main(pytest_args)