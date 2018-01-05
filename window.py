from PyQt5.QtWidgets import QApplication,QWidget,QDialog,QInputDialog
import sys
from untitled import Ui_Dialog
from untitled2 import Ui_Dialog2
import DivWords
import os
s = ["空","空","空"]
i = 0
st=[]
class wind(Ui_Dialog):

    def __init__(self,Dialog):
        self.setupUi(Dialog)



    def display_result(self,s):
        global i
        self.textBrowser_2.clear()
        self.textBrowser.clear()
        self.textBrowser_3.clear()
        if i+3 <= len(s):
            self.textBrowser.append(str(s[i]))
            self.textBrowser_2.append(str(s[i+1]))
            self.textBrowser_3.append((str(s[i+2])))
        elif i+2 == len(s):
            self.textBrowser.append(str(s[i]))
            self.textBrowser_2.append(str(s[i+1]))
            self.textBrowser_3.append("空")
        elif i+1 == len(s):
            self.textBrowser.append(str(s[i]))
            self.textBrowser_2.append("空")
            self.textBrowser_3.append("空")
        else:
            self.textBrowser.append("空")
            self.textBrowser_2.append("空")
            self.textBrowser_3.append("空")


    def next_page(self,s):
        self.textBrowser.clear()
        self.textBrowser_3.clear()
        self.textBrowser_2.clear()
        global i
        i = i+3
        self.display_result(st)

    def last_page(self,s):
        self.textBrowser.clear()
        self.textBrowser_3.clear()
        self.textBrowser_2.clear()
        global i
        i = i-3
        self.display_result(st)

    def get_input(self):
        s = self.lineEdit.text()
        global st
        if st:
            pass
        else:
            st = DivWords.search_indx(s)
        self.display_result(st)




class wind2(Ui_Dialog2):
    def __init__(self,Dialog):
        self.setupUi(Dialog)

    def get_indx(self):
        global s
        s = self.lineEdit.text()
        if os.path.isdir(s) == False:

            pass
        else:
            DivWords.Create_indx(s)
        w2.close()




app = QApplication(sys.argv)
w = QWidget()
ui = wind(w)
ui.setupUi(w)
w.show()
w2=QWidget()
ui2=wind2(w2)
ui2.setupUi(w2)
print(s)

ui.search.clicked.connect(lambda: ui.get_input())
ui.Creat_index.clicked.connect(lambda : w2.show())
ui.lastpage.clicked.connect(lambda: ui.last_page(s))
ui.nextpage.clicked.connect(lambda: ui.next_page(s))
ui2.OK.clicked.connect(lambda: ui2.get_indx())
ui2.Cancel.clicked.connect(lambda: w2.close())
ui.textBrowser.append("索引未建立！")
print(s)
sys.exit(app.exec())
print(s)
