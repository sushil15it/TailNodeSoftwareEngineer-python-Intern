import sqlite3
conn=sqlite3.connect('book.db')
Cursors=conn.cursor()
Cursors.execute('''CREATE TABLE book_detail(name TEXT,price DOUBLE,avilabilaty TEXT,rating TEXT)''')
