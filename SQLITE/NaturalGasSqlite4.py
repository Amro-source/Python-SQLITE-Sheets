# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 17:24:47 2021

@author: Zikantika
"""
import sqlite3
import pandas as pd 
import time
import datetime
import random
import os
import csv

con = sqlite3.connect("gas3.db")
cur = con.cursor()

con.execute('''CREATE TABLE COMPANY
         (DATE           TEXT    NOT NULL,
          PRICE          REAL     NOT NULL );''')
print ("Table created successfully");





a_file = open("naturalgasdaily.csv")
rows = csv.reader(a_file)

print(rows)
cur.executemany("INSERT INTO COMPANY VALUES (?, ?)", rows)

cur.execute("SELECT * FROM COMPANY")
print(cur.fetchall())

con.commit()
con.close()