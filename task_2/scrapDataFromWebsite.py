
from pickle import NONE
import sqlite3
import requests
from bs4 import BeautifulSoup


conn=sqlite3.connect('book.db')
cursor=conn.cursor()
name=price=avilabilaty=rating=NONE
url="http://books.toscrape.com"
#step 1
for page in range(1,51):
    print('page-no:'+str(page))
    response=requests.get(url + '/catalogue/page-'+ str(page)+'.html')
    htmlcontent=response.content
    #s2
    soup= BeautifulSoup(htmlcontent,'html.parser')
    headerdata=soup.find_all('li',class_='col-xs-6')
    for item in headerdata:
        bookname=price=avilabilaty0=rating1=NONE       
        bookname=item.h3.find('a').string
        price=item.find('div',class_='product_price').p.string
        avilabilaty=item.find('p',class_='availability').get('class')
        avilabilaty0=avilabilaty[0]
        rating=item.find('p',class_='star-rating').get('class')
        rating1=rating[1]
        cursor.execute('''INSERT INTO book_detail VALUES(?,?,?,?)''',(bookname,price,avilabilaty0,rating1))
        conn.commit()