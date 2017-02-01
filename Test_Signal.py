#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from pyqt5 import QtWidgets
def on_clicked():
    print("кнопка нажатияю функция on_clicked()")


class MyClass():
    def __init__(self,x=0):
        self.s=x
    def __call__(self):
        print('кнопка нажата')
        print("x=",self.x)
    def on_clicked(self):
        print("buttons clicket nazhata Myclass")
obj = MyClass
app = QtWidgets.QApplication(sys.argv)

button=QtWidgets.QPushButton("Clicked")

button.clicked.connect(on_clicked())
button.clicked.connect(obj.on_clicked())
button.clicked.connect(MyClass(10))
button.clicked.connect(lambda:)