# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'open.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
match=sqlite3.connect('cricket.db')
matchcur=match.cursor()


class Ui_FormO(object):
    def setupUi(self, FormO):
        FormO.setObjectName("FormO")
        FormO.resize(400, 300)
        FormO.setMinimumSize(QtCore.QSize(400, 300))
        FormO.setMaximumSize(QtCore.QSize(400, 300))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Image/cricket.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        FormO.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(FormO)
        self.label.setGeometry(QtCore.QRect(90, 50, 241, 91))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(FormO)
        self.pushButton.setGeometry(QtCore.QRect(140, 200, 93, 28))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.comboBox = QtWidgets.QComboBox(FormO)
        self.comboBox.setGeometry(QtCore.QRect(100, 130, 181, 31))
        self.comboBox.setObjectName("comboBox")

        self.retranslateUi(FormO)
        QtCore.QMetaObject.connectSlotsByName(FormO)

        teams= matchcur.execute("SELECT DISTINCT name FROM teams;")  # fetching team names
        y= teams.fetchall()
        for i in y:
            self.comboBox.addItem(i[0])

    def retranslateUi(self, FormO):
        _translate = QtCore.QCoreApplication.translate
        FormO.setWindowTitle(_translate("FormO", "Fantasy Cricket"))
        self.label.setText(_translate("FormO", "Enter Team Name :"))
        self.pushButton.setText(_translate("FormO", "OPEN"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FormO = QtWidgets.QWidget()
    ui = Ui_FormO()
    ui.setupUi(FormO)
    FormO.show()
    sys.exit(app.exec_())