#!/usr/bin/python
# -*- coding: utf-8 -*-


from PyQt5.QtWidgets import QTreeView,QApplication
from PyQt5 import QtSql
import sys
dbName = 'Cert2.db3'
con = QtSql.QSqlDatabase.addDatabase('QSQLITE')
con.setDatabaseName(dbName)
con.open()

class Main(QTreeView):
    def __init__(self):
        QTreeView.__init__(self)
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
        
        self.setModel(sqm)
        

    def test(self, signal):
        file_path=self.model()
        print(file_path)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Main()
    w.show()
    sys.exit(app.exec_())








#class Main(QTreeView):
#    def __init__(self):
##        QTreeView.__init__(self)
#        model = QFileSystemModel()
#        print(model)
#        model.setRootPath('C:\\')
#        self.setModel(model)
#        self.doubleClicked.connect(self.test)

    #def test(self, signal):
    #    file_path=self.model().filePath(signal)
    #    print(file_path)


#if __name__ == '__main__':
 #   import sys
 #   app = QApplication(sys.argv)
 #   w = Main()
 #   w.show()
  #  sys.exit(app.exec_())








