# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from points_calculator import player_points

from open import Ui_FormO as Open   # importing open window dialogbox
from new import Ui_new_2 as New     # importing new window dialogbox
from evaluate import Ui_FormE as Eva  # importing evaluate window dialogbox

import sqlite3
fant=sqlite3.connect('cricket.db')  # connecting to database file(fandatabase.db)
fantcurs=fant.cursor()

class Ui_MainWindow(object):
    def __init__(self):
        #NEW
        self.newDialog = QtWidgets.QMainWindow()
        self.new_screen = New()
        self.new_screen.setupUi(self.newDialog)

        #EVALUATE
        self.EvaluateWindow = QtWidgets.QMainWindow()
        self.eval_screen = Eva()
        self.eval_screen.setupUi(self.EvaluateWindow)

        #OPEN
        self.openDialog = QtWidgets.QMainWindow()
        self.open_screen = Open()
        self.open_screen.setupUi(self.openDialog)

    # FILE OPEN
    def file_open(self):
        self.open_screen.setupUi(self.openDialog)
        self.openDialog.show()
        self.open_screen.pushButton.clicked.connect(self.openteam)

    # EVALUATE TEAM MENU
    def file_evaluate(self):
        self.eval_screen.setupUi(self.EvaluateWindow)
        self.EvaluateWindow.show()

    def setupUi(self, MainWindow):
        # INITIALISING POINTS AND COUNTS
        self.avail_points = 1000
        self.used_points = 0
        self.totalcount = 0
        self.batsmencount = 0
        self.bowlerscount = 0
        self.alrdscount = 0
        self.wicketerscount = 0
        # INITIALIZING LISTS
        self.a = []  # bowler names list
        self.b = []  #  batsman nameslist
        self.c = []   # allrounder names list
        self.d = []  #wicketer names list
        self.list1 = []    # selectedplayer's list

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Image/cricket.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(40, 0, 721, 101))
        self.frame.setAutoFillBackground(False)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 10, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(9)
        font.setItalic(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.batsmen = QtWidgets.QLabel(self.frame)
        self.batsmen.setGeometry(QtCore.QRect(10, 50, 101, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)

        self.batsmen.setFont(font)
        self.batsmen.setObjectName("batsmen")
        self.bowlers = QtWidgets.QLabel(self.frame)
        self.bowlers.setGeometry(QtCore.QRect(170, 50, 121, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.bowlers.setFont(font)
        self.bowlers.setObjectName("bowlers")
        self.allrounder = QtWidgets.QLabel(self.frame)
        self.allrounder.setGeometry(QtCore.QRect(330, 50, 131, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.allrounder.setFont(font)
        self.allrounder.setObjectName("allrounder")
        self.wicket = QtWidgets.QLabel(self.frame)
        self.wicket.setGeometry(QtCore.QRect(500, 50, 171, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.wicket.setFont(font)
        self.wicket.setObjectName("wicket")
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setGeometry(QtCore.QRect(0, 30, 701, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        #BAT COUNT
        self.batcount = QtWidgets.QLabel(self.frame)
        self.batcount.setGeometry(QtCore.QRect(110, 50, 51, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.batcount.setFont(font)
        self.batcount.setObjectName("batcount")
        #BOWL COUNT
        self.bowlcount = QtWidgets.QLabel(self.frame)
        self.bowlcount.setGeometry(QtCore.QRect(270, 50, 51, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.bowlcount.setFont(font)
        self.bowlcount.setObjectName("bowlcount")
        #ALL ROUNDER COUNT
        self.allcount = QtWidgets.QLabel(self.frame)
        self.allcount.setGeometry(QtCore.QRect(440, 50, 51, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.allcount.setFont(font)
        self.allcount.setObjectName("allcount")
        #WICKET COUNT
        self.wcount = QtWidgets.QLabel(self.frame)
        self.wcount.setGeometry(QtCore.QRect(640, 50, 51, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.wcount.setFont(font)
        self.wcount.setObjectName("wcount")

        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(50, 110, 111, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")

        #POINT COUNT
        self.pointcount = QtWidgets.QLabel(self.centralwidget)
        self.pointcount.setGeometry(QtCore.QRect(160, 110, 51, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pointcount.setFont(font)
        self.pointcount.setObjectName("pointcount")
        #POINT USE
        self.pointuse = QtWidgets.QLabel(self.centralwidget)
        self.pointuse.setGeometry(QtCore.QRect(530, 110, 51, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pointuse.setFont(font)
        self.pointuse.setObjectName("pointuse")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(450, 110, 81, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        #AVAILABLE PLAYERS
        self.player = QtWidgets.QListWidget(self.centralwidget)
        self.player.setGeometry(QtCore.QRect(50, 190, 331, 351))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.player.setFont(font)
        self.player.setObjectName("player")
        #SELECTED PLAYERS
        self.select = QtWidgets.QListWidget(self.centralwidget)
        self.select.setGeometry(QtCore.QRect(450, 190, 311, 351))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.select.setFont(font)
        self.select.setObjectName("select")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(50, 150, 331, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        #RADIO BUTTONS
        #BAT
        self.bat = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.bat.setEnabled(False)
        self.bat.setObjectName("bat")
        self.horizontalLayout.addWidget(self.bat)
        #BOWL
        self.bow = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.bow.setEnabled(False)
        self.bow.setObjectName("bow")
        self.horizontalLayout.addWidget(self.bow)
        #ALL
        self.ar = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.ar.setEnabled(False)
        self.ar.setObjectName("ar")
        self.horizontalLayout.addWidget(self.ar)
        #WICKET
        self.wk = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.wk.setEnabled(False)
        self.wk.setObjectName("wk")
        self.horizontalLayout.addWidget(self.wk)

        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(450, 150, 311, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_15 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_2.addWidget(self.label_15)

        #TEAM NAME
        self.tname = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.tname.setFont(font)
        self.tname.setText("")
        self.tname.setObjectName("tname")
        self.horizontalLayout_2.addWidget(self.tname)
        MainWindow.setCentralWidget(self.centralwidget)
        #MENU BAR
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        #NEW TEAM
        self.actionNEW_Team = QtWidgets.QAction(MainWindow)
        self.actionNEW_Team.triggered.connect(self.file_new)
        self.actionNEW_Team.setObjectName("actionNEW_Team")
        #OPEN TEAM
        self.actionOPEN_Team = QtWidgets.QAction(MainWindow)
        self.actionOPEN_Team.triggered.connect(self.file_open)
        self.actionOPEN_Team.setObjectName("actionOPEN_Team")
        #SAVE TEAM
        self.actionSAVE_Team = QtWidgets.QAction(MainWindow)
        self.actionSAVE_Team.triggered.connect(self.file_save)
        self.actionSAVE_Team.setObjectName("actionSAVE_Team")
        #EVALUATE TEAM
        self.actionEVALUATE_Team = QtWidgets.QAction(MainWindow)
        self.actionEVALUATE_Team.triggered.connect(self.file_evaluate)
        self.actionEVALUATE_Team.setObjectName("actionEVALUATE_Team")
        self.menu.addAction(self.actionNEW_Team)
        self.menu.addSeparator()
        self.menu.addAction(self.actionOPEN_Team)
        self.menu.addSeparator()
        self.menu.addAction(self.actionSAVE_Team)
        self.menu.addSeparator()
        self.menu.addAction(self.actionEVALUATE_Team)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #DOUBLE CLICK
        self.player.itemDoubleClicked.connect(self.removelist1)
        self.select.itemDoubleClicked.connect(self.removelist2)

        #Stats of players
        self.stats = {}

        self.new_screen.create.clicked.connect(self.namechange)

        #RADIO BUTTON CLICKED
        self.bat.clicked.connect(self.load_names)
        self.wk.clicked.connect(self.load_names)
        self.bow.clicked.connect(self.load_names)
        self.ar.clicked.connect(self.load_names)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Fantasy Cricket"))
        self.label.setText(_translate("MainWindow", "Your Selections"))
        self.batsmen.setText(_translate("MainWindow", "Batsmen (BAT)"))
        self.bowlers.setText(_translate("MainWindow", "Bowlers (BOW)"))
        self.allrounder.setText(_translate("MainWindow", "Allrounder (AR)"))
        self.wicket.setText(_translate("MainWindow", "Wicker-Keeper (WK)"))
        self.batcount.setText(_translate("MainWindow", "##"))
        self.bowlcount.setText(_translate("MainWindow", "##"))
        self.allcount.setText(_translate("MainWindow", "##"))
        self.wcount.setText(_translate("MainWindow", "##"))
        self.label_10.setText(_translate("MainWindow", "Point Available :"))
        self.pointcount.setText(_translate("MainWindow", "####"))
        self.pointuse.setText(_translate("MainWindow", "####"))
        self.label_13.setText(_translate("MainWindow", "Point Used :"))
        self.bat.setText(_translate("MainWindow", "BAT"))
        self.bow.setText(_translate("MainWindow", "BOW"))
        self.ar.setText(_translate("MainWindow", "AR"))
        self.wk.setText(_translate("MainWindow", "WK"))
        self.label_15.setText(_translate("MainWindow", "Team Name :"))
        self.menu.setTitle(_translate("MainWindow", "Manage Teams"))
        self.actionNEW_Team.setText(_translate("MainWindow", "NEW Team"))
        self.actionOPEN_Team.setText(_translate("MainWindow", "OPEN Team"))
        self.actionSAVE_Team.setText(_translate("MainWindow", "SAVE Team"))
        self.actionEVALUATE_Team.setText(_translate("MainWindow", "EVALUATE Team"))

    # NEW FILE MENU
    def file_new(self):
        self.newDialog.show()

    def namechange(self):
        teamname = self.new_screen.lineEdit.text()
        fantcurs.execute("SELECT DISTINCT name FROM teams")
        l = fantcurs.fetchall()
        for i in l:
            if i[0] == teamname:
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText("Team with same name already exists!!\nPlease choose another name")
                msg.setWindowTitle("Invalid Team Name")
                msg.exec_()
                return 0
        if len(teamname) == 0:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("You cannot leave the field blank!!!")
            msg.setWindowTitle("Invalid Team Name")
            msg.exec_()
            return 0
        elif teamname.isnumeric():
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("Please enter a valid teamname\n(Name must contain atleast one character)!!")
            msg.setWindowTitle("Invalid Team Name")
            msg.exec_()
            return 0
        else:
            self.reset()
            self.t_name = self.new_screen.lineEdit.text()
            self.tname.setText('          '+self.t_name)
            self.newDialog.close()

    def reset(self):
        self.enablebuttons()
        self.load_names()
        self.used_points = 0
        self.alrdscount = 0
        self.wicketerscount = 0
        self.batsmencount = 0
        self.bowlerscount = 0
        self.totalcount = 0
        self.avail_points = 1000
        self.pointcount.setText(str(self.avail_points))
        self.pointuse.setText(str(self.used_points))
        self.bowlcount.setText(str(self.bowlerscount))
        self.batcount.setText(str(self.batsmencount))
        self.allcount.setText(str(self.alrdscount))
        self.wcount.setText(str(self.wicketerscount))
        self.list1.clear()
        self.load_names()

        self.select.clear()

    def file_save(self):
        if not self.error():  #IF THERE IS AN ERROR
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setInformativeText(' 😪Insufficient Players OR Points !!')
            msg.setWindowTitle("Fantasy Cricket")
            msg.exec_()
        elif self.error():  # IF NO ERROR
            try:
                fantcurs.execute("SELECT DISTINCT name FROM teams;")
                x = fantcurs.fetchall()
                for i in x:
                    if self.tname.text() == i[0]:   # CHECKING IF THE TEAMNAME ALREADY EXISTS
                        print('Updating already there')
                        fantcurs.execute("DELETE  FROM teams WHERE name='" + self.team_name.text() + "';") #DELETING TO UPDATE TEAM
            except:
                print('error')
            for i in range(self.select.count()):
                # print('----addding--')
                # print('teamnane: ',self.team_name.text())
                # print('playername: ',self.list1[i])
                # print('points: ', player_points[self.list1[i]])
                try:
                    fantcurs.execute("INSERT INTO teams (name,players,value) VALUES (?,?,?)",
                                     (self.tname.text(), self.list1[i], player_points[self.list1[i]]))

                    # self.file_evaluate()
                except:
                    print('error in operation!')
            fant.commit()
        else:
            print('---error in operation')

    def quit(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setInformativeText(' Bye 😙')
        msg.setWindowTitle("Fantasy Cricket")
        msg.exec_()
        # print('exit')
        sys.exit()

    #ON RADIO BUTTON CLICKED
    def load_names(self):
        Batsman = 'BAT'
        WicketKeeper = 'WK'
        Allrounder = 'AR'
        Bowler = 'BWL'
        sql1 = "SELECT player,value from stats WHERE ctg = '" + Batsman + "';"
        sql2 = "SELECT Player,value from stats WHERE ctg = '" + WicketKeeper + "';"
        sql3 = "SELECT Player,value from stats WHERE ctg ='" + Allrounder + "';"
        sql4 = "SELECT Player,value from stats WHERE ctg = '" + Bowler + "';"

        fantcurs.execute(sql1)
        x = fantcurs.fetchall()
        fantcurs.execute(sql4)
        y = fantcurs.fetchall()
        fantcurs.execute(sql3)
        z = fantcurs.fetchall()
        fantcurs.execute(sql2)
        w = fantcurs.fetchall()

        batsmen = []
        bowlers = []
        allrounders = []
        wcktkeepers = []

        for k in x:
            batsmen.append(k[0])
            self.b.append(k[0])
            self.stats[k[0]] = k[1]
        for k in y:
            bowlers.append(k[0])
            self.stats[k[0]] = k[1]
            self.a.append(k[0])
        for k in w:
            wcktkeepers.append(k[0])
            self.stats[k[0]] = k[1]
            self.d.append(k[0])
        for k in z:
            allrounders.append(k[0])
            self.stats[k[0]] = k[1]
            self.c.append(k[0])
        for i in self.list1:
            if i in allrounders:
                allrounders.remove(i)
            elif i in batsmen:
                batsmen.remove(i)
            elif i in bowlers:
                bowlers.remove(i)
            elif i in wcktkeepers:
                wcktkeepers.remove(i)

        if self.bat.isChecked() == True:
            self.player.clear()
            for i in range(len(batsmen)):
                item = QtWidgets.QListWidgetItem(batsmen[i])
                font = QtGui.QFont()
                font.setBold(True)
                font.setWeight(75)
                item.setFont(font)
                self.player.addItem(item)
        elif self.bow.isChecked() == True:
            self.player.clear()
            for i in range(len(bowlers)):
                item = QtWidgets.QListWidgetItem(bowlers[i])
                font = QtGui.QFont()
                font.setBold(True)
                font.setWeight(75)
                item.setFont(font)
                self.player.addItem(item)
        elif self.ar.isChecked() == True:
            self.player.clear()
            for i in range(len(allrounders)):
                item = QtWidgets.QListWidgetItem(allrounders[i])
                font = QtGui.QFont()
                font.setBold(True)
                font.setWeight(75)
                item.setFont(font)
                self.player.addItem(item)

        elif self.wk.isChecked() == True:
            self.player.clear()
            for i in range(len(wcktkeepers)):
                item = QtWidgets.QListWidgetItem(wcktkeepers[i])
                font = QtGui.QFont()
                font.setBold(True)
                font.setWeight(75)
                item.setFont(font)
                self.player.addItem(item)

    # REMOVE FROM AVAILABLE PLAYERS AND ADD TO SELECTED PLAYERS
    def removelist1(self, item):
        self.conditions_1(item.text())
        self.player.takeItem(self.player.row(item))
        self.select.addItem(item.text())
        self.totalcount = self.select.count()
        self.list1.append(item.text())
        self.error()

    # Adding and Deducting respective points from points_calculator.py
    def conditions_1(self, cat):
        self.avail_points -= self.stats[cat]
        self.used_points += self.stats[cat]
        if cat in self.a:
            self.bowlerscount += 1
        elif cat in self.d:
            self.wicketerscount += 1
        elif cat in self.c:
            self.alrdscount += 1
        elif cat in self.b:
            self.batsmencount += 1

        self.pointcount.setText(str(self.avail_points))
        self.pointuse.setText(str(self.used_points))
        self.bowlcount.setText(str(self.bowlerscount))
        self.batcount.setText(str(self.batsmencount))
        self.allcount.setText(str(self.alrdscount))
        self.wcount.setText(str(self.wicketerscount))

    # Adding and Deducting respective poinrs from points_calculator.py
    def conditions_2(self, cat):
        self.avail_points += self.stats[cat]
        self.used_points -= self.stats[cat]
        if cat in self.a:
            self.bowlerscount -= 1
        elif cat in self.d:
            self.wicketerscount -= 1
        elif cat in self.c:
            self.alrdscount -= 1
        elif cat in self.b:
            self.batsmencount -= 1

        self.pointcount.setText(str(self.avail_points))
        self.pointuse.setText(str(self.used_points))
        self.bowlcount.setText(str(self.bowlerscount))
        self.batcount.setText(str(self.batsmencount))
        self.allcount.setText(str(self.alrdscount))
        self.wcount.setText(str(self.wicketerscount))

    # REMOVE FROM SELECTED PLAYERS AND ADD TO AVAIALBLE PLAYERS
    def removelist2(self, item):
        self.select.takeItem(self.select.row(item))
        self.player.addItem(item.text())
        self.list1.remove(item.text())
        # self.error()
        self.totalcount = self.select.count()
        self.conditions_2(item.text())

    #upon open team selected
    def openteam(self):
        self.reset()
        teamname = self.open_screen.comboBox.currentText()
        self.tname.setText(teamname)
        self.enablebuttons()
        fantcurs.execute("SELECT players from teams WHERE name= '" + teamname + "';")
        x=fantcurs.fetchall()
        score=[]
        for i in x:
            fantcurs.execute("SELECT value from stats WHERE player='"+i[0]+"';")
            y=fantcurs.fetchone()
            score.append(y[0])
        # print(score)
        sum=0
        for i in score:
            sum+=i
        self.select.clear()
        self.load_names()
        for i in x:
            self.select.addItem(i[0])
            self.list1.append(i[0])
            self.conditions_1(i[0])
        self.used_points = sum
        self.avail_points = 1000 - sum
        self.pointcount.setText(str(self.avail_points))
        self.pointuse.setText(str(self.used_points))
        self.openDialog.close()


    def enablebuttons(self):
        self.bat.setEnabled(True)
        self.bow.setEnabled(True)
        self.ar.setEnabled(True)
        self.wk.setEnabled(True)


    def error(self):
        msg = QMessageBox()
        if self.wicketerscount > 1:
            msg.setIcon(QMessageBox.Critical)
            # msg.setText("Error")
            msg.setInformativeText('Only 1 wicketkeeper is allowed!')
            msg.setWindowTitle("Error")
            msg.exec_()
            return 0
        elif self.totalcount > 11:
            msg.setIcon(QMessageBox.Critical)
            msg.setInformativeText('No more than 11 players allowed!')
            msg.setWindowTitle("Selection Error")
            msg.exec_()
            return 0
        elif self.totalcount < 11 :
            return 0
        elif self.wicketerscount < 1:
            return 0
        elif self.avail_points <= -1:
            msg.setIcon(QMessageBox.Critical)
            msg.setInformativeText('Not enough points!')
            msg.setWindowTitle("Selection Cricket")
            msg.exec_()
            return 0

        return 1