# Library Management System

## **Project Overview**
This project is a Python-based **Library Management System (LMS)** designed to help users manage books and borrowing processes. It provides functionalities for user registration, book management, borrowing and returning books, tracking overdue books, and calculating fines. Additionally, the project focuses on testing these functionalities using **Unit Testing with `unittest`**.

---

## **Project Goals**
The primary goals of this project are to:

1. Develop a structured library management system with multiple functionalities.
2. Apply concepts of **Unit Testing with `unittest`** to validate the system.
3. Practice writing robust, maintainable, and reusable Python code.
4. Enhance debugging skills by identifying and addressing edge cases in testing.

---

## **Features**

### **1. User Management**
- **Registration**: Users can register with a unique username and password.
- **Login**: Users can log in to their accounts.

### **2. Book Management**
- Add books with attributes like title, author, genre, and count of available copies.
- Remove books by title.
- Search for books by title or author.

### **3. Borrowing/Returning Books**
- Users can borrow books if available.
- Borrowed books reduce the available count in the library.
- Users can return books, increasing the available count.

### **4. Overdue Tracking**
- Tracks overdue books and calculates fines based on the number of overdue days.
- Fine rate: **$1 per day past the return date**.

### **5. Admin Features**
- Perform CRUD operations on books.
- View overdue records and manage books effectively.

---

## **Directory Structure**
```
library_management/
├── app/
│   ├── __init__.py
│   ├── main.py            # Entry point of the application
│   ├── user.py            # User-related classes and functions
│   ├── book.py            # Book-related classes and functions
│   ├── borrowing.py       # Borrow/return logic
│   └── overdue.py         # Overdue fine calculation
├── tests/
│   ├── __init__.py
│   ├── test_user.py       # Unit tests for user-related features
│   ├── test_book.py       # Unit tests for book-related features
│   ├── test_borrowing.py  # Unit tests for borrow/return logic
│   └── test_overdue.py    # Unit tests for overdue calculations
└── README.md
```

---

## **Testing Details**

The project uses **Unit Testing with `unittest`** to validate each functionality:

1. **User Management**:
   - Test cases for successful registration and login.
   - Handle duplicate usernames and invalid login credentials.

2. **Book Management**:
   - Add and remove books.
   - Search for books by title and author.
   - Handle edge cases like non-existent books.

3. **Borrowing/Returning Books**:
   - Borrow books and update available copies.
   - Prevent borrowing unavailable books.
   - Test successful book returns.

4. **Overdue Tracking**:
   - Simulate overdue books and calculate fines accurately.
   - Validate fine calculation for edge cases.

---

## **How to Run the Project**

### **1. Clone the Repository**
```bash
git clone https://github.com/SCCSMARTCODE/Advanced-Python-Programming
cd library_management_system
```

### **2. Install Dependencies**
Ensure you have Python 3.x installed.

### **3. Run the Application**
Run the main application:
```bash
python app/main.py
```

### **4. Run Tests**
Execute unit tests to validate the system:
```bash
python -m unittest discover tests
```

---

## **Future Enhancements**
- Implement a graphical user interface (GUI).
- Integrate with a database for persistent storage.
- Add support for email notifications for overdue books.

---

## **Contributing**
Contributions are welcome! If you find any bugs or have suggestions for improvements, feel free to submit a pull request or open an issue.

---

## **License**
This project is licensed under the MIT License. See the LICENSE file for details.
