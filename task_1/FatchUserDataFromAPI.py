from email import header
import sqlite3
import requests
import json


conn=sqlite3.connect('user.db')
cursor=conn.cursor()
# c.execute('''CREATE TABLE user_detail(id TEXT,title TEXT,firstName TEXT,lastName TEXT,picture TEXT)''')
app_id='632f0e49b6b51c09f93b7243'
Headers={"app-id":app_id}
responses=requests.get('https://dummyapi.io/data/v1/user',headers=Headers)
UserData=responses.json()
# print(UserData)
# data from user data field
i=1
for user in UserData['data']:
    u_id=user['id']
    u_title =user['title']
    u_firstName =user['firstName']
    u_lastName=user['lastName'] 
    u_picture=user['picture']
    cursor.execute('''INSERT INTO user_detail VALUES(?,?,?,?,?)''',(u_id ,u_title,u_firstName,u_lastName,u_picture))
    conn.commit()
    print(str(i) +'row inserted')
    i+=1
