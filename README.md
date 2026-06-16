# Library Management System (Python + PostgreSQL)

A simple command-line based Library Management System built using **Python** and **PostgreSQL**. This project allows users to register, login, add books, view books, and issue books.

---

##  Features

- User Registration (Sign Up)
- User Login Authentication
- Add New Books
- View Available Books
- Issue Books to Users
- PostgreSQL Database Integration
- Book Quantity Management

---

##  Technologies Used

- Python 3
- PostgreSQL
- psycopg2

---

## Project Structure

```bash
project/
│
├── library_management_system.py              # Main Python file
├── README.md          # Project documentation
└── requirements.txt   # Dependencies
```

---

## Database Tables

### Users Table

| Column | Type |
|--------|------|
| user_id | Serial (Primary Key) |
| name | Text |
| father_name | Text |
| mother_name | Text |
| username | Varchar |
| pwd | Varchar |
| roll_no | Integer |

### Books Table

| Column | Type |
|--------|------|
| book_id | Serial (Primary Key) |
| title | Varchar |
| author | Text |
| quantity | Integer |

### Issued Books Table

| Column | Type |
|--------|------|
| issue_id | Serial (Primary Key) |
| user_id | Integer |
| book_id | Integer |
| issue_date | Date |

---

## 🔧 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/library-management-system.git
cd library-management-system
```

### 2. Install Dependencies

```bash
pip install psycopg2
```

Or create a `requirements.txt` file:

```txt
psycopg2
```

Then install:

```bash
pip install -r requirements.txt
```

### 3. Setup PostgreSQL

Create a database named:

```sql
CREATE DATABASE postgres;
```

Update your PostgreSQL credentials inside `gg.py`:

```python
conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="your_password",
    host="localhost",
    port="5432"
)
```

### 4. Create Database Tables

Run the following function once:

```python
table_user()
```

This creates:

- `users`
- `books`
- `issued_books`

---

## Running the Application

Execute the Python file:

```bash
python library_management_system.py
```

Main Menu:

```text
========= library system ============
1. sign up
2. login
3. exit
```

After successful login:

```text
========= library menu ============
1. Add book
2. View books
3. Issue books
4. Logout
```

---

##  Functionalities

### User Registration

New users can register by providing:

- Name
- Father's Name
- Mother's Name
- Username
- Password
- College Roll Number

### User Login

Users can login using:

- Username
- Password

### Add Books

Users can add books with:

- Title
- Author
- Quantity

### View Books

Displays all books available in the library.

### Issue Books

Books can be issued to users and available quantity is reduced automatically.

---

##  Known Issues

- Passwords are stored in plain text.
- Database credentials are hardcoded.
- No validation for duplicate usernames.
- Quantity may become negative if books are unavailable.
- `issue_date` and `issued_date` naming mismatch exists in code.
- Connections can be optimized using context managers.

---

##  Future Improvements

- Password hashing using `bcrypt`
- Return book feature
- Search books by title
- Admin authentication
- Fine calculation system
- GUI using Tkinter
- Web version using Flask/Django
- Email notifications

---

##  Contributing

Contributions are welcome.

1. Fork the repository
2. Create a branch

```bash
git checkout -b feature-name
```

3. Commit changes

```bash
git commit -m "Added new feature"
```

4. Push code

```bash
git push origin feature-name
```

5. Open a Pull Request

---

##  License

This project is licensed under the MIT License.

---
