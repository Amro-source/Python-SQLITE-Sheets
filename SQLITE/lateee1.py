# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 23:54:26 2021

@author: Zikantika
"""

import sqlite3

conn = sqlite3.connect('test.db')
print ("Opened database successfully");

conn.execute('''CREATE TABLE COMPANY
         (ID INT PRIMARY KEY     NOT NULL,
         NAME           TEXT    NOT NULL,
         AGE            INT     NOT NULL,
         ADDRESS        CHAR(50),
         SALARY         REAL);''')
print ("Table created successfully");

conn.close()