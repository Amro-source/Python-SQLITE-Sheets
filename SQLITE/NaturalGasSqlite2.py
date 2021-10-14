# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 16:44:17 2021

@author: Zikantika
"""

import sqlite3

conn = sqlite3.connect('gas.db')
print ("Opened database successfully");

cursor = conn.execute("SELECT id, DATE,PRICE from COMPANY")
for row in cursor:
   print ("ID = ", row[0])
   print ("DATE = ", row[1])
   print ("PRICE = ", row[2], "\n")

print ("Operation done successfully");
conn.close()