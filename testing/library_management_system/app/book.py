import json
from datetime import datetime, timedelta

BOOKS_DB = "db/books.json"


def load_books():
    try:
        with open(BOOKS_DB, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_books(books):
    with open(BOOKS_DB, "w") as file:
        json.dump(books, file, indent=4)


def add_book():
    books = load_books()
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    genre = input("Enter book genre: ")
    copies = int(input("Enter number of copies: "))

    book = {
        "title": title,
        "author": author,
        "genre": genre,
        "available_copies": copies,
        "borrowed_copies": 0,
        "transactions": []
    }

    books.append(book)
    save_books(books)
    print(f"Book '{title}' added successfully!\n")


def remove_book():
    books = load_books()
    title = input("Enter the title of the book to remove: ")
    books = [book for book in books if book["title"] != title]
    save_books(books)
    print(f"Book '{title}' removed successfully!\n")


def update_book():
    books = load_books()
    title = input("Enter the title of the book to update: ")
    for book in books:
        if book["title"] == title:
            book["author"] = input(f"Enter new author (current: {book['author']}): ") or book["author"]
            book["genre"] = input(f"Enter new genre (current: {book['genre']}): ") or book["genre"]
            book["available_copies"] = int(
                input(f"Enter new available copies (current: {book['available_copies']}): ") or book[
                    "available_copies"])
            save_books(books)
            print(f"Book '{title}' updated successfully!\n")
            return
    print(f"Book '{title}' not found!\n")


def view_all_books():
    books = load_books()
    if not books:
        print("No books available.\n")
        return

    print("\nAll Books:\n")
    for idx, book in enumerate(books, 1):
        print(
            f"{idx}. {book['title']} by {book['author']} ({book['genre']}) - Available: {book['available_copies']}, Borrowed: {book['borrowed_copies']}")
    print()


def borrow_book(user):
    books = load_books()
    title = input("Enter the title of the book to borrow: ")
    for book in books:
        if book["title"] == title:
            if book["available_copies"] > 0:
                book["available_copies"] -= 1
                book["borrowed_copies"] += 1
                borrow_date = datetime.now()
                due_date = borrow_date + timedelta(days=14)  # Two-week borrowing period
                transaction = {
                    "email": user.email,
                    "borrow_date": borrow_date.strftime("%Y-%m-%d"),
                    "due_date": due_date.strftime("%Y-%m-%d"),
                    "returned": False,
                    "charges": 0
                }
                book["transactions"].append(transaction)
                save_books(books)
                print(f"Book '{title}' borrowed successfully! Due date: {due_date.strftime('%Y-%m-%d')}\n")
                return
            else:
                print(f"Book '{title}' is currently unavailable.\n")
                return
    print(f"Book '{title}' not found!\n")


def return_book(user):
    books = load_books()
    title = input("Enter the title of the book to return: ")
    for book in books:
        if book["title"] == title:
            for transaction in book["transactions"]:
                if transaction["email"] == user.email and not transaction["returned"]:
                    return_date = datetime.now()
                    due_date = datetime.strptime(transaction["due_date"], "%Y-%m-%d")
                    transaction["returned"] = True

                    # Calculate charges for overdue books
                    if return_date > due_date:
                        overdue_days = (return_date - due_date).days
                        transaction["charges"] = overdue_days * 1  # $1 per overdue day
                        print(f"Book returned late by {overdue_days} days. Charges: ${transaction['charges']}\n")
                    else:
                        print(f"Book '{title}' returned on time. No charges.\n")

                    book["available_copies"] += 1
                    book["borrowed_copies"] -= 1
                    save_books(books)
                    return
            print(f"No record of '{title}' being borrowed by you.\n")
            return
    print(f"Book '{title}' not found!\n")