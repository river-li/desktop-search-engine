# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled2.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog2(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(701, 231)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../图片/baidu_85beaf5496f291521eb75ba38eacbd87.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(50, 100, 581, 41))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 50, 361, 31))
        self.label.setObjectName("label")
        self.OK = QtWidgets.QPushButton(Dialog)
        self.OK.setGeometry(QtCore.QRect(610, 180, 71, 31))
        self.OK.setObjectName("OK")
        self.Cancel = QtWidgets.QPushButton(Dialog)
        self.Cancel.setGeometry(QtCore.QRect(510, 180, 71, 31))
        self.Cancel.setObjectName("Cancel")

        self.retranslateUi(Dialog)
        self.lineEdit.editingFinished.connect(self.OK.click)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "建立新的索引"))
        self.label.setText(_translate("Dialog", "请输入要建立索引的目录位置："))
        self.OK.setText(_translate("Dialog", "OK"))
        self.Cancel.setText(_translate("Dialog", "Cancel"))

