# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mazeui.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(279, 222)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 0, 261, 171))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.button = QtWidgets.QCommandLinkButton(self.groupBox)
        self.button.setGeometry(QtCore.QRect(210, 70, 31, 31))
        self.button.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.button.setText("")
        self.button.setIconSize(QtCore.QSize(40, 40))
        self.button.setObjectName("button")
        self.box_gd = QtWidgets.QSpinBox(self.groupBox)
        self.box_gd.setGeometry(QtCore.QRect(80, 40, 61, 22))
        self.box_gd.setMinimum(1)
        self.box_gd.setMaximum(199)
        self.box_gd.setSingleStep(2)
        self.box_gd.setProperty("value", 99)
        self.box_gd.setObjectName("box_gd")
        self.xlcd = QtWidgets.QComboBox(self.groupBox)
        self.xlcd.setGeometry(QtCore.QRect(80, 120, 71, 22))
        self.xlcd.setObjectName("xlcd")
        self.xlcd.addItem("")
        self.xlcd.addItem("")
        self.xlcd.addItem("")
        self.xlcd.addItem("")
        self.box_kd = QtWidgets.QSpinBox(self.groupBox)
        self.box_kd.setGeometry(QtCore.QRect(81, 80, 61, 22))
        self.box_kd.setMinimum(1)
        self.box_kd.setMaximum(199)
        self.box_kd.setSingleStep(2)
        self.box_kd.setProperty("value", 99)
        self.box_kd.setObjectName("box_kd")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(30, 40, 41, 21))
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(30, 120, 41, 21))
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(30, 80, 41, 21))
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 279, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "迷宫生成"))
        self.xlcd.setItemText(0, _translate("MainWindow", "Kruscal"))
        self.xlcd.setItemText(1, _translate("MainWindow", "DFS"))
        self.xlcd.setItemText(2, _translate("MainWindow", "BFS"))
        self.xlcd.setItemText(3, _translate("MainWindow", "Recursive Division"))
        self.label.setText(_translate("MainWindow", "高度："))
        self.label_3.setText(_translate("MainWindow", "算法："))
        self.label_2.setText(_translate("MainWindow", "宽度："))

