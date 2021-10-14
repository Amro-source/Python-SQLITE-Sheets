# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 15:11:09 2021

@author: Zikantika
"""

import sqlite3
import pandas as pd 


df=pd.read_csv('naturalgasdaily.csv')  


print(df.head(10))

Prices=df['Price']

print(Prices)


conn = sqlite3.connect('gas.db')
print ("Opened database successfully");
#
conn.execute('''CREATE TABLE COMPANY
         (ID INT PRIMARY KEY     NOT NULL,
          DATE           TEXT    NOT NULL,
          PRICE          REAL     NOT NULL );''')
print ("Table created successfully");

conn.close()


conn = sqlite3.connect('gas.db')
print( "Opened database successfully");

conn.execute("INSERT INTO COMPANY (ID,DATE,PRICE) \
      VALUES (1, '1997-01-15', 4.34 )");

conn.execute("INSERT INTO COMPANY (ID,DATE,PRICE) \
      VALUES (2, '1997-01-16 ',  4.71 )");

conn.execute("INSERT INTO COMPANY (ID,DATE,PRICE) \
      VALUES (3, '1997-01-17', 3.91 )");

conn.execute("INSERT INTO COMPANY (ID,DATE,PRICE) \
      VALUES (4, '1997-01-20', 3.26 )");

conn.commit()
print ("Records created successfully");




