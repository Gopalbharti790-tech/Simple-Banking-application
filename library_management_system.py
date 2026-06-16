import psycopg2
from datetime import date
current_user=""
conn = psycopg2.connect(dbname="postgres", user="postgres", password="gopal", host="localhost", port="5432")
cursor = conn.cursor()

def table_user():
    global current_user,cursor
    conn = psycopg2.connect(dbname="postgres", user="postgres", password="gopal", host="localhost", port="5432")
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE users(
        name TEXT,
        father_name TEXT,
        mother_name TEXT,
        username VARCHAR,
        user_id serial primary key,
        pwd VARCHAR,
        roll_no INT
    )
    ''')
    cursor.execute('''
    CREATE TABLE books(
        book_id serial primary key,
        title varchar,
        author TEXT,
        quantity INT
    )
    ''')
    cursor.execute(''' create table issued_books(
        issue_id serial primary key,
        user_id int,
        book_id int,
        issue_date date,
        FOREIGN KEY(user_id) REFERENCES users(user_id),
        FOREIGN KEY(book_id) REFERENCES books(book_id))
    ''')
    print("Table created successfully")
    conn.commit()
    cursor.close()
    conn.close()


def signup():
    conn = psycopg2.connect(dbname="postgres", user="postgres", password="gopal", host="localhost", port="5432")
    cursor = conn.cursor()

    name = input("enter your name: ")
    father_name = input("enter your father name: ")
    mother_name = input("enter your mother name: ")
    username = input("create username: ")
    pwd = input("create password: ")
    roll_number = int(input("enter your college id: "))

    query = '''
    INSERT INTO users(name,father_name,mother_name,username,pwd,roll_no)
    VALUES (%s,%s,%s,%s,%s,%s)
    '''

    cursor.execute(query, (name, father_name, mother_name, username, pwd, roll_number))

    print("Data added successfully")
    conn.commit()
    conn.close()

def login():
    global current_user,cursor
    username=input("enter your user name : ")
    pwd=input("enter your password : ")
    cursor.execute("select user_id from users where username=%s and pwd=%s",(username,pwd))
    user=cursor.fetchone()
    if user:
        current_user=user[0]
        print("login successfully")
        library_menu()
    else:
        print("invalid username or password")
        
def add_books():
    
    title= input("Book title : ")
    author= input("Author name : ")
    quantity= int(input("Quantity of books : "))
    query='''insert into books
                   (title,author,quantity) values(%s,%s,%s)'''
    cursor.execute(query,(title,author,quantity))
    print("book added")
    
    
def view_books():
    cursor.execute('''select * from books''')
    books=cursor.fetchall()
    for book in books:
        print(book)
        
def issue_book():
    book_id=int(input("enter book id: "))
    user_id=int(input("enter user id : "))
    issued_book = int(input("enter the issue book : "))
    query1='''insert into issued_books(user_id,book_id,issued_date) values(%s,%s,%s)'''
    cursor.execute(query1,(user_id,book_id,issued_book))
    cursor.execute('''update books set quantity = quantity - 1 where book_id=%s''',(book_id,))
    conn.commit()
    print("book issue")
        
        
def library_menu():
    while True:
        print("\n ========= library menu ============")
        print("1. Add book")
        print("2. View books")
        print("3. Issue books")
        print("4. Logout")
        choose= input("enter your choice : ")
        if choose == "1":
            add_books()
        elif choose =="2":
            view_books()
        elif choose =="3":
            issue_book()
        elif choose == "4":
            break
        else:
            print("invalid choice")
while True:
        print("\n ========= library system ============")
        print("1. sign up")
        print("2. login")
        print("3. exit")
        choose= input("enter your choice : ")
        if choose == "1":
            signup()
        elif choose =="2":
            login()
        elif choose =="3":
            break
        else:
            print("invalid choice")