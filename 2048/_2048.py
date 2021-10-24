# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '2048.ui'
#
# Created by: PyQt5 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtWidgets.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def init_case(self, name, pos_x, pos_y):
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)

        case = QtWidgets.QLabel(self.widget)
        case.setGeometry(QtCore.QRect(pos_x, pos_y, 100, 100))
        case.setFont(font)
        case.setStyleSheet(_fromUtf8("background-color:#ffffde;"))
        case.setText(_fromUtf8(""))
        case.setTextFormat(QtCore.Qt.AutoText)
        case.setAlignment(QtCore.Qt.AlignCenter)
        case.setWordWrap(False)
        case.setObjectName(_fromUtf8(name))

        return case
    def show_in_popup(self, text):
        self.dial = QtWidgets.QDialog(self.centralwidget)
        self.dial.setWindowTitle(_translate("Help", "Aide", None))
        self.dial.setGeometry(QtCore.QRect(660, 500, 600, 150))
        label = QtWidgets.QLabel(self.dial)
        label.setText(text)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(75)
        label.setFont(font)
        label.setStyleSheet(_fromUtf8("padding: 20px;"))
        self.dial.setWindowModality(True)
        self.dial.show()

    def generate_grid(self):
        grid = []
        case_number = 1
        for i in range(4):
            pos_y = 10 + 110*i
            row = []
            for j in range(4):
                pos_x = 10 + 110*j 
                name = f"case0x0_{case_number}"
                case = self.init_case(name, pos_x, pos_y)
                row.append((case, (i, j)))
                case_number += 1
            grid.append(row)

        return grid

    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("2048"))
        MainWindow.resize(600, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.background = QtWidgets.QWidget(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, -20, 600, 600))
        self.background.setStyleSheet(_fromUtf8("background-color:#ffffff;"))
        self.background.setObjectName(_fromUtf8("background"))
        self.widget = QtWidgets.QWidget(self.background)
        self.widget.setGeometry(QtCore.QRect(75, 130, 450, 450))
        self.widget.setStyleSheet(_fromUtf8("background-color:#cacaca;"))
        self.widget.setObjectName(_fromUtf8("widget"))

        self.score = QtWidgets.QLabel(self.background)
        self.valScore = QtWidgets.QLabel(self.background)
        self.score.setGeometry(QtCore.QRect(10, 70, 71, 21))
        self.valScore.setGeometry(QtCore.QRect(80, 70, 45, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.score.setFont(font)
        self.score.setObjectName(_fromUtf8("score"))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.valScore.setFont(font)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        #self.pushButton = QtWidgets.QPushButton(self.background)
        #self.pushButton.setGeometry(QtCore.QRect(480, 80, 41, 31))
        #self.pushButton.setObjectName(_fromUtf8("pushButton"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("2048", "2048", None))
        self.score.setText(_translate("2048", "Score :", None))
        self.valScore.setText(_translate("2048", "0", None))
        #self.pushButton.setText(_translate("MainWindow", "retour", None))

