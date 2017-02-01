# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QTreeView
#from PyQt5.QtWidgets import QMenu
from PyQt5.QtGui import QStandardItemModel, QStandardItem
#from PyQt5.QtCore import QPoint
from PyQt5 import QtSql
import sys
dbPath = 'Cert2.db3'
app = QApplication(sys.argv)
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
__author__ = 'Moon_'
class TreeView(QTreeView):
    #currentitem = None     # Здесь сохраняю выбранный item(modelindex) после обработки события от мыши
                                     # заново присваиваю None
    def __init__(self):
        QTreeView.__init__(self)
        self.pressed.connect(self.presseditem)

    def presseditem(self, modelindex):
        self.currentitem = modelindex
if __name__ == '__main__':
  
    widget = QWidget()
    widget.resize(200, 600)
    treeview = TreeView()
    layout = QVBoxLayout()
    layout.addWidget(treeview)
    widget.setLayout(layout)
    model = QStandardItemModel()
    model.setHorizontalHeaderLabels(['Форма'])

    UnitDb = dbQl("""select u.Name from Unit as u""")
    print(UnitDb)
    for UnitName in UnitDb:
        item_u = QStandardItem(UnitName)
        sqlUnitS = ('select us.Name from Unit as u, UnitSubject as us'
                    ' WHERE 1=1'
                    ' and u.id=us.idPodr'
                    ' and u.name ="'
                    + UnitName +'"')
        UnitSDb = dbQl(sqlUnitS)
        
        print(sqlUnitS)
        for UnitSName in UnitSDb:
            item_uu = item_u.appendRows([QStandardItem(UnitSName)])



        itemroot = model.invisibleRootItem()
        itemroot.appendRow(item_u)
    treeview.setModel(model)
    widget.show()
    sys.exit(app.exec_())