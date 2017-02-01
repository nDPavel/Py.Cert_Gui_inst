#!/usr/bin/python
# -*- coding: utf-8 -*-
from PyQt5 import QtCore,QtWidgets,QtSql

import sys
dbName = 'Cert2.db3'
app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QTreeView()
window.setWindowTitle("QSqlQeryModel")
con = QtSql.QSqlDatabase.addDatabase('QSQLITE')
con.setDatabaseName(dbName)
con.open()

sqm = QtSql.QSqlQueryModel()
sqm.setQuery("""select   u.Name,
                         us.Name
                         --,cd.DateCre
                         --,cd.DateExp
                         --,cd.PodrName
                         --,cd.UserName
                         --,cd.password
                         --,cd."Path"
                         from Unit as U,
                              UnitSubject as us,
                              CertDate as cd,
                              LinkCertORUnitSub as link
                              WHERE 1=1
                              and link.idPodr = us.id
                              and link.IdCert = cd.id
                              and U.id = us.idPodr
                              --and us.Name = 'Alapaevsk'

""")
#
sqm.setHeaderData(0, QtCore.Qt.Horizontal,'Region')
sqm.setHeaderData(1, QtCore.Qt.Horizontal,'Podr')
#sqm.setHeaderData(2, QtCore.Qt.Horizontal,'DateCre')
#sqm.setHeaderData(3, QtCore.Qt.Horizontal,'DateExp')
#sqm.setHeaderData(4, QtCore.Qt.Horizontal,'L=')
##sqm.setHeaderData(5, QtCore.Qt.Horizontal,'CN=')
#sqm.setHeaderData(6, QtCore.Qt.Horizontal,'Pass')
#sqm.setHeaderData(7, QtCore.Qt.Horizontal,'Path')

window.setModel(sqm)

#window.hideColumn(0)
window.resize(700,300)
window.show()
sys.exit(app.exec_())














