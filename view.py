# @Author: Абделлах Улахияне
# @Date:   2021-04-11 04:21:08
# @Last Modified by:   Абделлах Улахияне
# @Last Modified time: 2021-04-11 16:48:54
# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from db import db
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import QCoreApplication, QMetaObject
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(311, 392)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.commands = QtWidgets.QTabWidget(self.centralwidget)
        self.commands.setObjectName("commands")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.figureid = QtWidgets.QLineEdit(self.tab)
        self.figureid.setObjectName("figureid")
        self.horizontalLayout.addWidget(self.figureid)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.figurename = QtWidgets.QLineEdit(self.tab)
        self.figurename.setObjectName("figurename")
        self.horizontalLayout_2.addWidget(self.figurename)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.figureimgpath = QtWidgets.QLabel(self.tab)
        self.figureimgpath.setText("")
        self.figureimgpath.setObjectName("figureimgpath")
        self.horizontalLayout_3.addWidget(self.figureimgpath)
        self.btnfigureimgpath = QtWidgets.QPushButton(self.tab)
        self.btnfigureimgpath.setObjectName("btnfigureimgpath")
        self.horizontalLayout_3.addWidget(self.btnfigureimgpath)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.figuredescription = QtWidgets.QTextEdit(self.tab)
        self.figuredescription.setObjectName("figuredescription")
        self.horizontalLayout_4.addWidget(self.figuredescription)
        self.gridLayout_2.addLayout(self.horizontalLayout_4, 3, 0, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.btnaddgfigure = QtWidgets.QPushButton(self.tab)
        self.btnaddgfigure.setObjectName("btnaddgfigure")
        self.horizontalLayout_5.addWidget(self.btnaddgfigure)
        self.btnupdatefigure = QtWidgets.QPushButton(self.tab)
        self.btnupdatefigure.setObjectName("btnupdatefigure")
        self.horizontalLayout_5.addWidget(self.btnupdatefigure)
        self.btndeletefigure = QtWidgets.QPushButton(self.tab)
        self.btndeletefigure.setObjectName("btndeletefigure")
        self.horizontalLayout_5.addWidget(self.btndeletefigure)
        self.gridLayout_2.addLayout(self.horizontalLayout_5, 4, 0, 1, 1)
        self.commands.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_8.addWidget(self.label_5)
        self.commandid = QtWidgets.QLineEdit(self.tab_2)
        self.commandid.setObjectName("commandid")
        self.horizontalLayout_8.addWidget(self.commandid)
        self.gridLayout_3.addLayout(self.horizontalLayout_8, 0, 0, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_7.addWidget(self.label_6)
        self.commandlabel = QtWidgets.QLineEdit(self.tab_2)
        self.commandlabel.setObjectName("commandlabel")
        self.horizontalLayout_7.addWidget(self.commandlabel)
        self.gridLayout_3.addLayout(self.horizontalLayout_7, 1, 0, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_7 = QtWidgets.QLabel(self.tab_2)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_6.addWidget(self.label_7)
        self.commanddescription = QtWidgets.QTextEdit(self.tab_2)
        self.commanddescription.setObjectName("commanddescription")
        self.horizontalLayout_6.addWidget(self.commanddescription)
        self.gridLayout_3.addLayout(self.horizontalLayout_6, 2, 0, 1, 1)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.btnaddcommand = QtWidgets.QPushButton(self.tab_2)
        self.btnaddcommand.setObjectName("btnaddcommand")
        self.horizontalLayout_9.addWidget(self.btnaddcommand)
        self.btnupdatecommand = QtWidgets.QPushButton(self.tab_2)
        self.btnupdatecommand.setObjectName("btnupdatecommand")
        self.horizontalLayout_9.addWidget(self.btnupdatecommand)
        self.btndeletecommand = QtWidgets.QPushButton(self.tab_2)
        self.btndeletecommand.setObjectName("btndeletecommand")
        self.horizontalLayout_9.addWidget(self.btndeletecommand)
        self.gridLayout_3.addLayout(self.horizontalLayout_9, 3, 0, 1, 1)
        self.commands.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_8 = QtWidgets.QLabel(self.tab_3)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_10.addWidget(self.label_8)
        self.guideid = QtWidgets.QLineEdit(self.tab_3)
        self.guideid.setObjectName("guideid")
        self.horizontalLayout_10.addWidget(self.guideid)
        self.gridLayout_4.addLayout(self.horizontalLayout_10, 0, 0, 1, 3)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_9 = QtWidgets.QLabel(self.tab_3)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_11.addWidget(self.label_9)
        self.guidelabel = QtWidgets.QLineEdit(self.tab_3)
        self.guidelabel.setObjectName("guidelabel")
        self.horizontalLayout_11.addWidget(self.guidelabel)
        self.gridLayout_4.addLayout(self.horizontalLayout_11, 1, 0, 1, 3)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_10 = QtWidgets.QLabel(self.tab_3)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_12.addWidget(self.label_10)
        self.guidedescription = QtWidgets.QTextEdit(self.tab_3)
        self.guidedescription.setObjectName("guidedescription")
        self.horizontalLayout_12.addWidget(self.guidedescription)
        self.gridLayout_4.addLayout(self.horizontalLayout_12, 2, 0, 1, 3)
        self.btnaddguide = QtWidgets.QPushButton(self.tab_3)
        self.btnaddguide.setObjectName("btnaddguide")
        self.gridLayout_4.addWidget(self.btnaddguide, 3, 0, 1, 1)
        self.btnupdateguide = QtWidgets.QPushButton(self.tab_3)
        self.btnupdateguide.setObjectName("btnupdateguide")
        self.gridLayout_4.addWidget(self.btnupdateguide, 3, 1, 1, 1)
        self.btndeleteguide = QtWidgets.QPushButton(self.tab_3)
        self.btndeleteguide.setObjectName("btndeleteguide")
        self.gridLayout_4.addWidget(self.btndeleteguide, 3, 2, 1, 1)
        self.commands.addTab(self.tab_3, "")
        self.gridLayout.addWidget(self.commands, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.commands.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Chess Telegram Bot Management", "Chess Telegram Bot Management"))
        self.label.setText(_translate("MainWindow", "ID                 "))
        self.label_2.setText(_translate("MainWindow", "NAME           "))
        self.label_4.setText(_translate("MainWindow", "IMAGE PATH"))
        self.btnfigureimgpath.setText(_translate("MainWindow", "..."))
        self.label_3.setText(_translate("MainWindow", "DESCRIPTION"))
        self.btnaddgfigure.setText(_translate("MainWindow", "Add"))
        self.btnupdatefigure.setText(_translate("MainWindow", "Update"))
        self.btndeletefigure.setText(_translate("MainWindow", "Delete"))
        self.commands.setTabText(self.commands.indexOf(self.tab), _translate("MainWindow", "byade9"))
        self.label_5.setText(_translate("MainWindow", "ID           "))
        self.label_6.setText(_translate("MainWindow", "Label      "))
        self.label_7.setText(_translate("MainWindow", "Description"))
        self.btnaddcommand.setText(_translate("MainWindow", "Add"))
        self.btnupdatecommand.setText(_translate("MainWindow", "Update"))
        self.btndeletecommand.setText(_translate("MainWindow", "Delete"))
        self.commands.setTabText(self.commands.indexOf(self.tab_2), _translate("MainWindow", "commands"))
        self.label_8.setText(_translate("MainWindow", "ID           "))
        self.label_9.setText(_translate("MainWindow", "LABEL     "))
        self.label_10.setText(_translate("MainWindow", "Description"))
        self.btnaddguide.setText(_translate("MainWindow", "Add"))
        self.btnupdateguide.setText(_translate("MainWindow", "Update"))
        self.btndeleteguide.setText(_translate("MainWindow", "Delete"))
        self.commands.setTabText(self.commands.indexOf(self.tab_3), _translate("MainWindow", "guide"))
        self.init()

    def init(self):
        self.btnaddgfigure.clicked.connect(      self.click_btnaddfigure)
        self.btnupdatefigure.clicked.connect(self.click_btnupdatefigure)
        self.btndeletefigure.clicked.connect(self.click_btndeletefigure)
        self.btnfigureimgpath.clicked.connect(self.click_btnfigureimgpath)

        self.btnaddcommand.clicked.connect(      self.click_btnaddcommand)
        self.btnupdatecommand.clicked.connect(self.click_btnupdatecommand)
        self.btndeletecommand.clicked.connect(self.click_btndeletecommand)

        self.btnaddguide.clicked.connect(      self.click_btnaddguide)
        self.btnupdateguide.clicked.connect(self.click_btnupdateguide)
        self.btndeleteguide.clicked.connect(self.click_btndeleteguide)

    def click_btnaddfigure(self):
        db.add("figures",{'id':self.figureid.text(),"name":self.figurename.text(),"imgpath":self.figureimgpath.text(),"description":self.figuredescription.toPlainText()})
    def click_btnupdatefigure(self):
        db.update("figures",{"name":self.figurename.text(),"imgpath":self.figureimgpath.text(),"description":self.figuredescription.toPlainText()},{'id':self.figureid.text()})
    def click_btndeletefigure(self):
        db.delete("figures",{'id':self.figureid.text()})
    def click_btnfigureimgpath(self):
        fname = QFileDialog.getOpenFileName(directory="images")
        self.figureimgpath.setText(fname[0]) if len(fname)>0 else self.figureimgpath.setText("")

    def click_btnaddcommand(self):
        db.add("commands",{'id':self.commandid.text(),"label":self.commandlabel.text(),"description":self.commanddescription.toPlainText()})
    def click_btnupdatecommand(self):
        db.update("commands",{"label":self.commandlabel.text(),"description":self.commanddescription.toPlainText()},{'id':self.commandid.text()})

    def click_btndeletecommand(self):
        db.delete("commands",{'id':self.commandid.text()})

    def click_btnaddguide(self):
        db.add("guide",{'id':self.guideid.text(),"label":self.guidelabel.text(),"description":self.guidedescription.toPlainText()})

    def click_btnupdateguide(self):
        db.update("guide",{"label":self.guidelabel.text(),"description":self.guidedescription.toPlainText()},{'id':self.guideid.text()})

    def click_btndeleteguide(self):
        db.delete("guide",{'id':self.guideid.text()})




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
