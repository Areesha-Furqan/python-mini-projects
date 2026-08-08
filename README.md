# Python Learning Journey

This repository contains beginner-to-intermediate Python scripts I built while mastering fundamental concepts like lists, loops, conditionals, and user interaction. Each project is a fully functional CLI application with zero external dependencies—just pure Python logic.

---

## Projects Included:

### 1. 🛒 [Shopping Cart](https://github.com/Areesha-Furqan/python-mini-projects/blob/main/shopping_cart.py)
A menu-driven CLI program that simulates an interactive shopping cart. Users can manage their cart through a numbered menu with real-time feedback.

- **Concepts Covered:** `append`, `insert`, `remove`, `pop`, `clear`, `sort`, `len`, conditional checks (`in`), and infinite `while` loops.
- **Features:** Add items, insert at specific positions, remove by exact name, remove the last item, view cart, count items, empty cart, and exit gracefully.

### 2. 📚 [Community Library Loan Manager](https://github.com/Areesha-Furqan/python-mini-projects/blob/main/Community_Library_Loan_Manager.py)
A comprehensive CLI tool for a small community library to manage its book collection. Starts with a pre-set inventory and lets librarians borrow, return, add, and reorganize books through a 13-option menu.

- **Concepts Covered:** `append`, `insert`, `remove`, `pop`, `clear`, `sort`, `reverse`, `len`, `in` operator, negative indexing (`[-1]`), safe removal with pre-validation, and confirmation dialogs.
- **Features:** View all books, borrow a book (with safety check), return a book, add a new book, insert at any position, check availability, total count, peek at the last book, undo the last action, sort alphabetically, reverse order, empty the entire collection (with confirmation), and exit.

### 3. 📊 [Gradebook Manager](https://github.com/Areesha-Furqan/python-mini-projects/blob/main/Student_Gradebook_Manager.py)
A comprehensive CLI tool for a teacher to manage student grades using dictionary-based key-value storage. Starts with a pre-set gradebook and allows adding, updating, deleting, searching, and merging student records through a 13-option menu.

- **Concepts Covered:** Dictionary operations (`keys`, `values`, `items`, `get`, `setdefault`, `popitem`, `update`, `copy`, `clear`), `in` operator, `del`, `len`, safe lookups, confirmation dialogs, and infinite `while` loops.

- **Features:** View all students and grades, add a new student, update a grade, delete a student (with safety check), safely retrieve a grade using `.get()`, check if a student exists, add a student only if missing (`.setdefault()`), remove the last added student (`.popitem()`), count total students, copy the gradebook as a backup, merge another gradebook, clear all grades (with confirmation), and exit gracefully.

### 4. 🎓 [Student Course Enrollment System](https://github.com/Areesha-Furqan/python-mini-projects/blob/main/student_course_enrollment_system.py)
A comprehensive CLI system for university departments to manage student enrollments. Handles adding students, enrolling them in courses, dropping courses, and generating reports using nested data structures (dictionary of students → each with a list of courses).

- **Concepts Covered:** `Function definition`, `parameters`, `return` values, refactoring procedural code into modular functions, safe data handling via parameters instead of `global` variables, `nested dictionaries`, dictionary of dictionaries with lists, `.items()`, `.copy()`, `.setdefault()`, `in` operator, `del`, `len`, `nested loops`, course counting using a temporary dictionary, case-insensitive `search`, confirmation dialogs, and safe data validation.

- **Features:** `Function definition`, `parameters`, `return` values, refactoring procedural code into modular functions, safe data handling via parameters instead of `global` variables, `nested dictionaries`, dictionary of dictionaries with lists, `.items()`, `.copy()`, `.setdefault()`, `in` operator, `del`, `len`, `nested loops`, course counting using a temporary dictionary, case-insensitive `search`, confirmation dialogs, and safe data validation.

### 5. 💰 [Personal Expense Tracker](https://github.com/Areesha-Furqan/python-mini-projects/blob/main/personal_expense_tracker.py)
A comprehensive CLI tool for personal finance management. Tracks income and expenses, generates category-wise summaries, monthly breakdowns, and budget comparisons using a list-of-dictionaries data structure.

- **Concepts Covered:** `Function definition`, `parameters`, `return` values, `list` of dictionaries, `dictionary` aggregation, date `filtering`, case-insensitive `search`, `combined-key` budgeting, budget vs actual `comparisons`, safe `deletion` with confirmation, `docstrings`, and `modular function-based architecture`.

- **Features:** Add transaction (auto-ID), view all transactions, view expense summary by category, view monthly summary (income/expenses/net savings), delete transaction (with confirmation), search transactions (case-insensitive partial match), set monthly budget per category, check budget status (compare spending against budget), and exit gracefully.

### 6. 📦 [SmartStock Inventory System](https://github.com/Areesha-Furqan/python-mini-projects/blob/main/smart_stock_inventory_system.py)
A professional CLI inventory management system for small retail shops. Track products, manage stock levels, receive low-stock alerts, and prevent overselling—all with automatic JSON persistence.

- **Concepts Covered:** List of dictionaries, functions with parameters and return values, error handling (`try/except` with bulletproof input loops), JSON file I/O (`json.dump()`/`json.load()`), low-stock alert logic, oversell prevention, deletion confirmation, deleted products log, docstrings, and modular function-based architecture.
- **Features:** Add new product (auto-ID), view all products (with `❗❗LOW STOCK❗❗` warnings), `search` by name/category (`case-insensitive`), reduce stock quantity (prevents overselling), increase stock quantity, permanently remove product (with confirmation), automatic data persistence, and bulletproof `error handling` for all user inputs.

---

## Purpose
To build a solid foundation in Python logic, data manipulation, and control flow before advancing to dictionaries, file handling, and object-oriented programming. Every script is written with clean structure, meaningful variable names, and inline comments for readability.

## How to Run
1. Navigate to any project folder.
2. Run the script using:  
   `python filename.py`
3. Follow the on-screen menu prompts.

---

