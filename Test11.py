#!/usr/bin/python3
# -*- coding: utf-8 -*-
#http://www.linux.org.ru/forum/development/1788460
#http://ps.readthedocs.io/ru/latest/strings.html
#http://stackoverflow.com/questions/41204234/python-pyqt5-qtreewidget-sub-item
#http://ru.stackoverflow.com/questions/511955/pyqt5-Контекстное-меню-только-на-элементах-qtreewidget
#http://stackoverflow.com/questions/11608276/extract-data-from-db-then-pass-it-to-qtreeview


import sys
from PyQt5.QtWidgets import QTreeWidget, QTreeWidgetItem, QApplication, QWidget
from PyQt5 import QtSql

dbPath = 'Cert2.db3'

app = QApplication(sys.argv)

con = QtSql.QSqlDatabase.addDatabase('QSQLITE')
con.setDatabaseName('Cert2.db3')
con.open()
query = QtSql.QSqlQuery()
query.exec_("""select   u.Name,
                        us.Name,
                        cd.DateCre,
                        cd.DateExp,
                        cd.PodrName,
                        cd.UserName
                            from Unit as U,
                                 UnitSubject as us,
                                 CertDate as cd,
                                 LinkCertORUnitSub as link
                                            WHERE 1=1
                                            and link.idPodr = us.id
                                            and link.IdCert = cd.id
                                            and U.id = us.idPodr
                                            and us.Name = 'Alapaevsk'
""")
lst = []
if query.isActive():
    query.first()
   
    while query.isValid():
        lst.append(query.value('Name'))
        query.next()
      
#print(p)
if __name__ == '__main__':
    app = 0
    if QApplication.instance():
        app = QApplication.instance()
    else:
        app = QApplication(sys.argv)
    
    #print(lst)
    
    
    i=0
    for p in lst: 
        lst[i] = p
        #print(lst[i])
        
    l0 = QTreeWidgetItem(['ddd'])
    #l2 = QTreeWidgetItem([p])

    for i in range(3):
        l0_child = QTreeWidgetItem(["Child A" + str(i)])
        l0.addChild(l0_child)

    #for j in range(2):
     #   l2_child = QTreeWidgetItem(["Child AA" + str(j)])
     #   l2.addChild(l2_child)

    w = QWidget()
    w.resize(510, 210)

    tw = QTreeWidget(w)
    tw.resize(500, 200)
    #количество столбцов
    tw.setColumnCount(1)
    tw.addTopLevelItem(QTreeWidgetItem(l0))
    #tw.addTopLevelItem(l2)

    w.show()
    con.close()
    sys.exit(app.exec_())





