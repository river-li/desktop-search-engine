# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(740, 754)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../图片/baidu_85beaf5496f291521eb75ba38eacbd87.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.search = QtWidgets.QPushButton(Dialog)
        self.search.setGeometry(QtCore.QRect(590, 30, 141, 41))
        self.search.setObjectName("search")
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 30, 581, 41))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 100, 711, 161))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.verticalLayoutWidget_2)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_2.addWidget(self.textBrowser)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 270, 711, 171))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.verticalLayoutWidget_3)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.verticalLayout_3.addWidget(self.textBrowser_2)
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(10, 450, 711, 181))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.verticalLayoutWidget_4)
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.verticalLayout_4.addWidget(self.textBrowser_3)
        self.nextpage = QtWidgets.QPushButton(Dialog)
        self.nextpage.setGeometry(QtCore.QRect(470, 670, 101, 41))
        self.nextpage.setObjectName("nextpage")
        self.lastpage = QtWidgets.QPushButton(Dialog)
        self.lastpage.setGeometry(QtCore.QRect(590, 670, 101, 41))
        self.lastpage.setObjectName("lastpage")
        self.Creat_index = QtWidgets.QPushButton(Dialog)
        self.Creat_index.setGeometry(QtCore.QRect(310, 670, 101, 41))
        self.Creat_index.setObjectName("Creat_index")

        self.retranslateUi(Dialog)
        self.lineEdit.editingFinished.connect(self.search.click)
        self.nextpage.clicked.connect(self.textBrowser.clear)
        self.nextpage.clicked.connect(self.textBrowser_2.clear)
        self.nextpage.clicked.connect(self.textBrowser_3.clear)
        self.lastpage.clicked.connect(self.textBrowser_3.clear)
        self.lastpage.clicked.connect(self.textBrowser_2.clear)
        self.lastpage.clicked.connect(self.textBrowser.clear)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "文本搜索器"))
        self.search.setText(_translate("Dialog", "搜索"))
        self.nextpage.setText(_translate("Dialog", "下一页"))
        self.lastpage.setText(_translate("Dialog", "上一页"))
        self.Creat_index.setText(_translate("Dialog", "建立索引"))

