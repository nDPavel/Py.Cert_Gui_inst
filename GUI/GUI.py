# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MyForm(object):
    def setupUi(self, MyForm):
        MyForm.setObjectName("MyForm")
        MyForm.resize(712, 663)
        self.verticalLayoutWidget = QtWidgets.QWidget(MyForm)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 10, 301, 181))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.btnQuit = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btnQuit.setObjectName("btnQuit")
        self.verticalLayout.addWidget(self.btnQuit)
        self.treeWidget = QtWidgets.QTreeWidget(MyForm)
        self.treeWidget.setGeometry(QtCore.QRect(0, 200, 256, 192))
        self.treeWidget.setObjectName("treeWidget")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_3 = QtWidgets.QTreeWidgetItem(item_2)
        self.treeView = QtWidgets.QTreeView(MyForm)
        self.treeView.setGeometry(QtCore.QRect(320, 210, 256, 192))
        self.treeView.setObjectName("treeView")

        self.retranslateUi(MyForm)
        QtCore.QMetaObject.connectSlotsByName(MyForm)

    def retranslateUi(self, MyForm):
        _translate = QtCore.QCoreApplication.translate
        MyForm.setWindowTitle(_translate("MyForm", "Test_Gui"))
        self.label.setText(_translate("MyForm", "TextLabel"))
        self.btnQuit.setText(_translate("MyForm", "Exit"))
        self.treeWidget.headerItem().setText(0, _translate("MyForm", "1"))
        self.treeWidget.headerItem().setText(1, _translate("MyForm", "Новый столбец"))
        self.treeWidget.headerItem().setText(2, _translate("MyForm", "Новый столбец"))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, _translate("MyForm", "Новый элемент"))
        self.treeWidget.topLevelItem(0).child(0).setText(0, _translate("MyForm", "Новый дочерний элемент"))
        self.treeWidget.topLevelItem(0).child(0).child(0).setText(0, _translate("MyForm", "Новый дочерний элемент"))
        self.treeWidget.topLevelItem(0).child(0).child(0).child(0).setText(0, _translate("MyForm", "Новый дочерний элемент"))
        self.treeWidget.setSortingEnabled(__sortingEnabled)





if __name__=='GUI':
    import  sys
    app = QtWidgets.QApplication(sys.argv)
    window = Ui_MyForm()
    window.show()
    sys.exit(app.exec_())