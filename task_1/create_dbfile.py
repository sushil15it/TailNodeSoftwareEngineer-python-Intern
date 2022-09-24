import sqlite3
conn=sqlite3.connect('user.db')
c=conn.cursor()
c.execute('''CREATE TABLE user_detail(id TEXT,title TEXT,firstName TEXT,lastName TEXT,picture TEXT)''')
c.execute('''CREATE TABLE user_post_data(id TEXT,image TEXT,likes int,tags,text TEXT,publishdate TEXT)''')
