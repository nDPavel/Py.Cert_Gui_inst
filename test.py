#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt5 import QtSql, QtWidgets
import sys, os

dbPath = r'./DB/Cert2.db3'
if os.path.exists(dbPath): 
    print ("Файл найден")
else: 
    print ("Файл не найден")

app = QtWidgets.QApplication(sys.argv)
con = QtSql.QSqlDatabase.addDatabase('QSQLITE')

a = con.setDatabaseName('Cert2.db')
print(a)
con.open()
query = QtSql.QSqlQuery()
query.exec_("SELECT * FROM Unit")
lst = []
#if query.isActive():
#    query.first()
#    while query.isValid():
#        lst.append(query.value('id')+':'+ str(query.value('Name')))
#        query.next()
#    for p in lst: print(p)
con.close()



