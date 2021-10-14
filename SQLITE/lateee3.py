# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 14:35:28 2021

@author: Zikantika
"""

import sqlite3

conn = sqlite3.connect('test.db')
print ("Opened database successfully");

cursor = conn.execute("SELECT id, name, address, salary from COMPANY")
for row in cursor:
   print ("ID = ", row[0])
   print ("NAME = ", row[1])
   print ("ADDRESS = ", row[2])
   print ("SALARY = ", row[3], "\n")

print ("Operation done successfully");
conn.close()