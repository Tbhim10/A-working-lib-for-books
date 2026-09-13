import sqlite3
link = sqlite3.connect("Library.db")
cursor = link.cursor()

cursor.execute("PRAGMA foreign_keys = ON;")
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Users(
        User_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL,
        role TEXT NOT NULL
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Books(
        book_id INTEGER PRIMARY KEY AUTOINCREMENT,
        Book_title TEXT NOT NULL UNIQUE,
        Author TEXT NOT NULL,
        total_copies INTEGER NOT NULL,
        available_copies INTEGER
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS borrow_recoerds (
        U_id INTEGER,
        B_id INTEGER,
        date_borrowed INTEGER,
        due_date INTEGER,
        return_date INTEGER,

        FOREIGN KEY(U_id) REFERENCES Users(User_id),
        FOREIGN KEY(B_id) REFERENCES Bookss(book_id)
    )
""")

link.commit()
print("Tables added successfully")