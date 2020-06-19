# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'evaluate.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from score import Ui_FormS as Score  #Score window
import sqlite3
match= sqlite3.connect("cricket.db")
matchcur=match.cursor()

class Ui_FormE(object):
    def __init__(self):  #initialising score window
        self.scoreDialog = QtWidgets.QMainWindow()
        self.score_screen = Score()
        self.score_screen.setupUi(self.scoreDialog)
    
    def setupUi(self, FormE):
        FormE.setObjectName("FormE")
        FormE.resize(616, 581)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Image/cricket.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        FormE.setWindowIcon(icon)
        self.frame = QtWidgets.QFrame(FormE)
        self.frame.setGeometry(QtCore.QRect(20, 0, 571, 101))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(80, 0, 401, 31))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setGeometry(QtCore.QRect(60, 50, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox_2 = QtWidgets.QComboBox(self.frame)
        self.comboBox_2.setGeometry(QtCore.QRect(330, 50, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.listWidget = QtWidgets.QListWidget(FormE)
        self.listWidget.setGeometry(QtCore.QRect(50, 170, 231, 291))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.listWidget.setFont(font)
        self.listWidget.setObjectName("listWidget")
        self.verticalScrollBar = QtWidgets.QScrollBar(FormE)
        self.verticalScrollBar.setGeometry(QtCore.QRect(260, 169, 20, 291))
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.listWidget_2 = QtWidgets.QListWidget(FormE)
        self.listWidget_2.setGeometry(QtCore.QRect(350, 170, 231, 291))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.listWidget_2.setFont(font)
        self.listWidget_2.setObjectName("listWidget_2")
        self.verticalScrollBar_2 = QtWidgets.QScrollBar(FormE)
        self.verticalScrollBar_2.setGeometry(QtCore.QRect(560, 170, 20, 291))
        self.verticalScrollBar_2.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar_2.setObjectName("verticalScrollBar_2")
        self.pushButton = QtWidgets.QPushButton(FormE)
        self.pushButton.setGeometry(QtCore.QRect(220, 500, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(FormE)
        self.label_2.setGeometry(QtCore.QRect(60, 140, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(FormE)
        self.label_3.setGeometry(QtCore.QRect(350, 140, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(FormE)
        self.label_4.setGeometry(QtCore.QRect(430, 140, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setText("")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")

        self.retranslateUi(FormE)
        QtCore.QMetaObject.connectSlotsByName(FormE)

         # score button
        self.pushButton.clicked.connect(self.final_score)
        selected_team = self.comboBox.currentText()

        self.changedname(selected_team)

        #upon current text changed
        self.comboBox.currentTextChanged.connect(self.changedname)

    def retranslateUi(self, FormE):
        _translate = QtCore.QCoreApplication.translate
        FormE.setWindowTitle(_translate("FormE", "Fantasy Cricket"))
        self.label.setText(_translate("FormE", "Evaluate the Performance of your Fantasy Team"))
        self.comboBox_2.setItemText(0, _translate("FormE", "Select Match"))
        self.comboBox_2.setItemText(1, _translate("FormE", "Match 1"))
        self.pushButton.setText(_translate("FormE", "Calculate Score"))
        self.label_2.setText(_translate("FormE", "Players"))
        self.label_3.setText(_translate("FormE", "Points :"))

        x = matchcur.execute("SELECT  DISTINCT name from teams;")
        team = x.fetchall()
        for i in team:
            self.comboBox.addItem(i[0])

    def changedname(self, t):
        self.listWidget.clear()
        self.listWidget_2.clear()
        y = matchcur.execute("SELECT players from teams WHERE name='" + t + "';")
        player = y.fetchall()
        # print('player',player)
        for j in player:
            self.listWidget.addItem(j[0])
        z = matchcur.execute("SELECT value from teams WHERE name='" + t + "';")
        value = z.fetchall()
        for k in value:
            self.listWidget_2.addItem(str(k[0]))


    def final_score(self):
        total_score=0
        t=self.comboBox.currentText()   # current teamname
        # print(t)
        z = matchcur.execute("SELECT value from teams WHERE name='" + t + "';")
        value = z.fetchall()
        # print('value', value)
        for k in value:
            total_score+=k[0]
        self.score_screen.lineEdit.setText(str(total_score))  # opening score dialog box and setting final score
        self.scoreDialog.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FormE = QtWidgets.QWidget()
    ui = Ui_FormE()
    ui.setupUi(FormE)
    FormE.show()
    sys.exit(app.exec_())