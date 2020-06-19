# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'score.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FormS(object):
    def setupUi(self, FormS):
        FormS.setObjectName("FormS")
        FormS.resize(400, 300)
        font = QtGui.QFont()
        font.setPointSize(10)
        FormS.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Image/cricket.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        FormS.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(FormS)
        self.label.setGeometry(QtCore.QRect(90, 60, 211, 61))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(FormS)
        self.lineEdit.setGeometry(QtCore.QRect(110, 120, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")

        self.retranslateUi(FormS)
        QtCore.QMetaObject.connectSlotsByName(FormS)

    def retranslateUi(self, FormS):
        _translate = QtCore.QCoreApplication.translate
        FormS.setWindowTitle(_translate("FormS", "Fantasy Cricket"))
        self.label.setText(_translate("FormS", "Your Team Score :"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FormS = QtWidgets.QWidget()
    ui = Ui_FormS()
    ui.setupUi(FormS)
    FormS.show()
    sys.exit(app.exec_())
