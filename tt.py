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
        print(query.value('Name'))
        lst.append(query.value('Name'))
        query.next()
        #print(lst)
        
        
        
    con.close()
    sys.exit(app.exec_())





