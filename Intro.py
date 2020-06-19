# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Intro.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from main import Ui_MainWindow

class Ui_Fantasy(object):
    #open new
    def mainscr(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        Fantasy.hide()
        self.window.show()
        
    def setupUi(self, Fantasy):
        Fantasy.setObjectName("Fantasy")
        Fantasy.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Fantasy.sizePolicy().hasHeightForWidth())
        Fantasy.setSizePolicy(sizePolicy)
        Fantasy.setMinimumSize(QtCore.QSize(800, 600))
        Fantasy.setMaximumSize(QtCore.QSize(800, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Image/cricket.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Fantasy.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(Fantasy)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(210, 0, 371, 341))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Image/218293_cricket-logo-png-removebg-preview.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(240, 300, 271, 91))
        font = QtGui.QFont()
        font.setFamily("Chiller")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(310, 400, 131, 81))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.horizontalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.start = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.start.setFont(font)
        self.start.setObjectName("start")
        self.verticalLayout.addWidget(self.start)
        self.exit = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.exit.setFont(font)
        self.exit.setObjectName("exit")
        self.verticalLayout.addWidget(self.exit)
        Fantasy.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Fantasy)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName("menubar")
        Fantasy.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Fantasy)
        self.statusbar.setObjectName("statusbar")
        Fantasy.setStatusBar(self.statusbar)

        self.retranslateUi(Fantasy)
        self.exit.clicked.connect(Fantasy.close)
        QtCore.QMetaObject.connectSlotsByName(Fantasy)

        #START
        self.start.clicked.connect(self.mainscr)
        

    def retranslateUi(self, Fantasy):
        _translate = QtCore.QCoreApplication.translate
        Fantasy.setWindowTitle(_translate("Fantasy", "Fantasy Cricket"))
        self.label_2.setText(_translate("Fantasy", "Fantasy Cricket"))
        self.start.setText(_translate("Fantasy", "START"))
        self.exit.setText(_translate("Fantasy", "EXIT"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Fantasy = QtWidgets.QMainWindow()
    ui = Ui_Fantasy()
    ui.setupUi(Fantasy)
    Fantasy.show()
    sys.exit(app.exec_())
