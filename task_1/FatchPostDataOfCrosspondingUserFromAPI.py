import sqlite3
from unittest import result
import requests
import json

conn=sqlite3.connect('user.db')
cursor=conn.cursor()
# c.execute('''CREATE TABLE user_post_data(id TEXT,image TEXT,likes int,tags TEXT,text TEXT,publishdate TEXT)''')
app_id='632f0e49b6b51c09f93b7243'
Headers={"app-id":app_id}
cursor.execute('''SELECT id from user_detail''')
result=cursor.fetchall()
for user in result:
    userid=user[0]
    response=requests.get('https://dummyapi.io/data/v1/user/' + userid + '/post',headers=Headers) 
    postdata=response.json()
    i=1
    for post in postdata['data']:
        cursor.execute('''INSERT INTO user_post_data VALUES(?,?,?,?,?,?)''',(post['id'],post['image'],post['likes'],' '.join(map(str, post['tags'])), post['text'],post['publishDate']))
        conn.commit()
        print('user '+userid+'  post no '+str(i) +' inserted')
        i+=1 