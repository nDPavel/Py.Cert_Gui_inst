#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QTreeWidget, QTreeWidgetItem, QApplication, QWidget
from PyQt5 import QtSql

dbPath = 'Cert2.db3'

app = QApplication(sys.argv)
def dbQl(ql):
    con = QtSql.QSqlDatabase.addDatabase('QSQLITE')
    con.setDatabaseName('Cert2.db3')
    #ql="""select * from Unit as U"""
    con.open()
    query = QtSql.QSqlQuery()
    query.exec_(ql)
    lst = []
    if query.isActive():
        query.first()
        while query.isValid():
            lst.append(query.value("Name"))
            query.next()
        #i=0
        #print(lst)
        #for p in lst: 
        #    p#lst[i] = p
        #    print(p)
            #print(lst[i])
        #    con.close()
    return lst
#dbQl("""select * from Unit limit 2""")

UnitSDb = dbQl("""select us.Name from Unit as u, UnitSubject as us
                                    WHERE 1=1
                                    and u.id=us.idPodr
                                    and u.name = 'Ekaterinburg'""")
print(UnitSDb)




sys.exit(app.exec_())




