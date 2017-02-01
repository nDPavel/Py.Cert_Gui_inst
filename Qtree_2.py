#!/usr/bin/python3
# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets, QtGui
import sys

def on_clicked():
    ind = view.currentIndex()
    if ind.isValid():
        print("Данные:", ind.data())
        print("row:", ind.row(), "column:", ind.column())
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

        ind_sibling = ind.sibling(0, 0)
        if ind_sibling.isValid():
            print("sibling:", ind_sibling.data())
        else:
            print("Нет sibling")

    else:
        print("Нет текущего элемента")

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QTreeView")
window.resize(500, 400)
view = QtWidgets.QTreeView()

model = QtGui.QStandardItemModel()
model.setColumnCount(4)
item1 = QtGui.QStandardItem("Корневой элемент 1")
model.appendRow(item1)
item2 = QtGui.QStandardItem("Корневой элемент 2")
model.appendRow(item2)
item3 = QtGui.QStandardItem("Корневой элемент 2")
model.appendRow(item3)

index_item1 = model.indexFromItem(item1)
model.insertRows(0, 3, parent=index_item1)
model.insertColumns(0, 4, parent=index_item1)
for row in range(0, 3):
    for column in range(0, 4):
        model.setData(model.index(row, column, parent=index_item1), 
                      "({0}, {1})".format(row, column))

index_item2 = model.indexFromItem(item2)
model.insertRows(0, 3, parent=index_item2)
model.insertColumns(0, 4, parent=index_item2)
for row in range(0, 3):
    for column in range(0, 4):
        model.setData(model.index(row, column, parent=index_item2), 
                      "({0}, {1})".format(row, column))

view.setModel(model)

button = QtWidgets.QPushButton("Получить значения")
button.clicked.connect(on_clicked)
box = QtWidgets.QVBoxLayout()
box.addWidget(view)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec_())