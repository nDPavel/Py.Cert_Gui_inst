#!/usr/bin/python3
# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets, QtGui
from PyQt5 import QtSql
import sys
dbPath = 'Cert2.db3'

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

def on_clicked():
    ind = view.currentIndex()
    if ind.isValid():
        print("Данные:", ind.data())

        ind_parent = ind.parent()
        if ind_parent.isValid():
            print("Родитель:", ind_parent.data())
        else:
            print("Нет родителя")

        ind_child = ind.child(0, 0)
        if ind_child.isValid():
            print("child:", ind_child.data())
        else:
            print("Нет child")

    else:
        print("Нет текущего элемента")

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QTreeView")
window.resize(500, 500)
view = QtWidgets.QTreeView()

model = QtGui.QStandardItemModel()
model.setColumnCount(2)
UnitDb = dbQl("""select u.Name from Unit as u""")
for UnitName in UnitDb:
    
    item1 = QtGui.QStandardItem(UnitName)
    sqlUnitS = ('select us.Name from Unit as u, UnitSubject as us'
                    ' WHERE 1=1'
                    ' and u.id=us.idPodr'
                    ' and u.name ="'
                    + UnitName + '"')
    UnitSDb = dbQl(sqlUnitS)
    print(UnitSDb)
    for UnitSName in UnitSDb:
        #item1.appendRow(UnitSName)
        item1.appendRows([QtGui.QStandardItem(UnitSName)])
    model.appendRow(item1)

'''
index_item2 = model.indexFromItem(item2)
model.insertRows(0, 3, parent=index_item2)
model.insertColumns(0, 4, parent=index_item2)
for row in range(0, 3):
    for column in range(0, 4):
        model.setData(model.index(row, column, parent=index_item2), 
                      "({0}, {1})".format(row, column))
'''
view.setModel(model)

button = QtWidgets.QPushButton("Получить значения")
button.clicked.connect(on_clicked)
box = QtWidgets.QVBoxLayout()
box.addWidget(view)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec_())