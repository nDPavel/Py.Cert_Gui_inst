#!/usr/bin/python3
# -*- coding: utf-8 -*-


from PyQt5.QtWidgets import QTreeWidget, QTreeWidgetItem, QApplication, QWidget
from PyQt5 import QtSql, QtGui
import sys

dbPath = 'Cert2.db3'
#app = QApplication(sys.argv)
#########################Функци обращения к бд###########################################
def dbQl(ql): #функция запроса к бд
    con = QtSql.QSqlDatabase.addDatabase('QSQLITE') #Выбираем драйвер для работы с бд
    con.setDatabaseName('Cert2.db3')#определяем путь к бд
    con.open()#открываем соединение
    query = QtSql.QSqlQuery()
    query.exec_(ql)
    lst = []
    if query.isActive():
        query.first()
        while query.isValid():
            lst.append(query.value("Name"))
            query.next()
        return lst
#############################################################################################
if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = QWidget()
    tw = QTreeWidget(w)
    tw.resize(500, 600)
    tw.setColumnCount(3)
    tw.setHeaderLabels(["reg"])
   
    UnitDb = dbQl("""select u.Name from Unit as u""")
    print(UnitDb)
    for UnitName in UnitDb:
        l1 = QTreeWidgetItem([UnitName])
        sqlUnitS = ('select us.Name from Unit as u, UnitSubject as us'
                    ' WHERE 1=1'
                    ' and u.id=us.idPodr'
                    ' and u.name ="'
                    + UnitName + '"')
        UnitSDb = dbQl(sqlUnitS)
        print(sqlUnitS)
        for UnitSName in UnitSDb:
            l1_child = QTreeWidgetItem([UnitSName])
            l1.addChild(l1_child)
            tw.addTopLevelItem(l1)
    def test(self, signal):
        filePath=3
        filePath(signal)
        print("ff")
            
    
    
    
w.resize(510, 610)
w.show()
sys.exit(app.exec_())






















