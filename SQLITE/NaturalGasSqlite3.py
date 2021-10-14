# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 16:52:06 2021

@author: Zikantika
"""

import sqlite3
import pandas as pd 
import time
import datetime
import random

conn = sqlite3.connect('gas.db')
print ("Opened database successfully");

df=pd.read_csv('naturalgasdaily.csv')  


print(df.head(10))

Prices=df['Price']
Dates=df['Date']

print(Prices)

print(len(Prices))

for i in range(5,len(Prices)):
   print(Prices[i]) 
   print(Dates[i]) 
   date=Dates[i]
   price=Prices[i]
#   id=i
   conn.execute("INSERT INTO COMPANY (ID,DATE,PRICE) \
      VALUES ( 'i','date','price' )");

conn = sqlite3.connect('gas.db')
print ("Opened database successfully");
#
#conn.execute('''CREATE TABLE COMPANY
#         (ID INT PRIMARY KEY     NOT NULL,
#          DATE           TEXT    NOT NULL,
#          PRICE          REAL     NOT NULL );''')
#print ("Table created successfully");
#
#conn.close()



print(df.describe)



#def dynamic_data_entry():
#
##    unix = int(time.time())
##    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
##    keyword = 'Python'
##    value = random.randrange(0,10)
#
#    conn.execute("INSERT INTO COMPANY (ID,DATE,PRICE) \
#      VALUES (id, date,price )");
#
#    conn.commit()
#    
#c.execute("INSERT INTO People VALUES('userName', 'password', 'confirmPassword', 'firstName','lastName', 'companyName', 'email', phoneNumber,'addressLine1', 'addressLine2', 'addressLine3', zipCode, 'province', 'country', 'regDate')")    
    

#conn = sqlite3.connect('gas.db')
#print( "Opened database successfully");

#conn.execute("INSERT INTO COMPANY (ID,DATE,PRICE) \
#      VALUES (1, '1997-01-15', 4.34 )");
#
#conn.execute("INSERT INTO COMPANY (ID,DATE,PRICE) \
#      VALUES (2, '1997-01-16 ',  4.71 )");
#
#conn.execute("INSERT INTO COMPANY (ID,DATE,PRICE) \
#      VALUES (3, '1997-01-17', 3.91 )");
#
#conn.execute("INSERT INTO COMPANY (ID,DATE,PRICE) \
#      VALUES (4, '1997-01-20', 3.26 )");
#
#conn.commit()
#print ("Records created successfully");

