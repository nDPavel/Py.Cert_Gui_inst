#!/usr/bin/env python

  
  
import sys
  
from PyQt5.QtWidgets import QApplication, QTreeView#, QFileSystemModel
from PyQt5 import QtSql  

dbName = 'Cert2.db3'
con = QtSql.QSqlDatabase.addDatabase('QSQLITE')
con.setDatabaseName(dbName)
con.open()
app = QApplication(sys.argv)
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
#model = QFileSystemModel()

#sqm.setData("sqm")

tree = QTreeView()
tree.setModel(sqm)
  
tree.setAnimated(False)
tree.setIndentation(20)
tree.setSortingEnabled(True)
  
tree.setWindowTitle("Dir View")

tree.resize(640, 480)
tree.show()
con.close()  
sys.exit(app.exec_())