#!/usr/bin/python
# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets, QtSql
import sys
app = QtWidgets.QApplication(sys.argv)
con = QtSql.QSqlDatabase.addDatabase('QSQLITE')
con.setDatabaseName('data3.sqlite')
con.open()
if 'good' not in con.tables():
    query = QtSql.QSqlQuery()
    query.exec("create table good(id integer primary key autoincrement,goodname text, goodcount integer)")
    con.transaction()
    query.prepare("insert into good values(null, ?, ?)")
    query.addBindValue('Дискета')
    query.addBindValue(10)
    query.exec_()
    query.prepare("insert into good values(null, ?, ?)")
    query.bindValue(0, 'Компакт-диск')
    query.bindValue(1, 4)
    query.exec_()
    query.prepare("insert into good values(null, :name, :count)")
    query.bindValue(':name', 'Коврик для мыши')
    query.bindValue(':count', 1)
    query.exec_()
    con.commit()
con.close()





























