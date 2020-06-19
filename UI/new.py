# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_new_2(object):
    def setupUi(self, new_2):
        new_2.setObjectName("new_2")
        new_2.resize(400, 300)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Image/cricket.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        new_2.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(new_2)
        self.label.setGeometry(QtCore.QRect(60, 60, 281, 71))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(new_2)
        self.lineEdit.setGeometry(QtCore.QRect(70, 130, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.create = QtWidgets.QPushButton(new_2)
        self.create.setGeometry(QtCore.QRect(130, 230, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.create.setFont(font)
        self.create.setObjectName("create")

        self.retranslateUi(new_2)
        QtCore.QMetaObject.connectSlotsByName(new_2)

    def retranslateUi(self, new_2):
        _translate = QtCore.QCoreApplication.translate
        new_2.setWindowTitle(_translate("new_2", "Fantasy Cricket"))
        self.label.setText(_translate("new_2", "Enter New Team Name :"))
        self.create.setText(_translate("new_2", "SAVE"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    new_2 = QtWidgets.QWidget()
    ui = Ui_new_2()
    ui.setupUi(new_2)
    new_2.show()
    sys.exit(app.exec_())
