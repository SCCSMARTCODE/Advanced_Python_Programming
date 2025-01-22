import json
import os

from book import add_book, remove_book, update_book, view_all_books, borrow_book, return_book

# Path to the JSON file storing user data
USER_DATA_FILE = "db/user_data.json"

# Ensure the file exists
if not os.path.exists(USER_DATA_FILE):
    with open(USER_DATA_FILE, "w") as f:
        json.dump([], f)


class UserObj:
    def __init__(self, username, email, mode):
        self.username = username
        self.email = email
        self.mode = mode

    def __repr__(self):
        return f"UserObj(username='{self.username}', email='{self.email}', mode='{self.mode}')"


def register() -> UserObj:
    """
    Register a new user and save the details to the JSON file.
    Returns:
        UserObj: The newly created user object.
    """
    username = input("Enter your username: ").strip()
    email = input("Enter your Gmail (must be unique): ").strip()
    password = input("Enter your password: ").strip()
    mode = input("Enter your mode (admin/client): ").strip().lower()

    if mode not in ["admin", "client"]:
        print("Invalid mode. Please choose 'admin' or 'client'.")
        return None

    # Load existing user data
    with open(USER_DATA_FILE, "r") as f:
        users = json.load(f)

    # Check for unique email
    for user in users:
        if user["email"] == email:
            print("This email is already registered. Please use a different Gmail.")
            return None

    # Create and save the new user
    new_user = {
        "username": username,
        "email": email,
        "password": password,
        "mode": mode
    }
    users.append(new_user)

    with open(USER_DATA_FILE, "w") as f:
        json.dump(users, f, indent=4)

    print("Registration successful!")
    return UserObj(username, email, mode)


def login() -> UserObj:
    """
    Log in an existing user by verifying their username and password.
    Returns:
        UserObj: The logged-in user object.
    """
    email = input("Enter your Gmail: ").strip()
    password = input("Enter your password: ").strip()

    # Load existing user data
    with open(USER_DATA_FILE, "r") as f:
        users = json.load(f)

    # Authenticate user
    for user in users:
        if user["email"] == email and user["password"] == password:
            print("Login successful!")
            return UserObj(user["username"], user["email"], user["mode"])

    print("Invalid Gmail or password. Please try again.")
    return None


def client_menu(user):
    print("\nUser Menu")
    print("----------")
    print("1. Search for a Book")
    print("2. Borrow a Book")
    print("3. Return a Book")
    print("4. View Borrowed Books")
    print("5. Logout")

    while True:
        choice = input("Please select an option: ")
        if choice == '1':
            view_all_books()
        elif choice == '2':
            borrow_book(user=user)
        elif choice == '3':
            return_book(user=user)
        elif choice == '4':
            view_all_books()
        elif choice == '5':
            print("Logging out...\n")
            break
        else:
            print("Invalid option. Please try again.\n")
            continue


def admin_menu():
    print("\nAdmin Menu")
    print("-----------")
    print("1. Add New Book")
    print("2. Remove Book")
    print("3. Update Book Details")
    print("4. View All Books")
    print("5. Logout")

    while True:

        choice = input("Please select an option: ")
        if choice == '1':
            add_book()
        elif choice == '2':
            remove_book()
        elif choice == '3':
            update_book()
        elif choice == '4':
            view_all_books()
        elif choice == '5':
            print("Logging out...\n")
            break
        else:
            print("Invalid option. Please try again.\n")
            continue

