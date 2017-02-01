#!/usr/bin/python
# -*- coding: utf-8 -*-


from PyQt5 import QtSql, QtWidgets
import sys, os

dbPath = 'Cert2.db3'
print(dbPath)
if os.path.exists(dbPath): 
    print (u"фаил найден")
else: 
    print (u"фаил не найден")

app = QtWidgets.QApplication(sys.argv)
#назначаем
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
    for p in lst: print(p)
con.close()

