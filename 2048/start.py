from _2048 import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5 import QtGui, QtWidgets, QtCore
import os, sys
from random import randint 
import marshal

class MainWindow(QMainWindow, Ui_MainWindow):
	def __init__(self, parent=None):

		QMainWindow.__init__(self, parent)
		self.setupUi(self)
		self.row_0 = [self.case0x0, self.case0x0_2, self.case0x0_3, self.case0x0_4]
		self.row_1 = [self.case0x0_5, self.case0x0_6, self.case0x0_7, self.case0x0_8]
		self.row_2 = [self.case0x0_9, self.case0x0_10, self.case0x0_11, self.case0x0_12]
		self.row_3 = [self.case0x0_13, self.case0x0_14, self.case0x0_15, self.case0x0_16]
		self.grille = [self.row_0, self.row_1, self.row_2, self.row_3]
		self.grid = []
		self.popup("tuto")
		self.genGrid()
		self.randNum()
		self.Score()

	def popup(self, arg="end"):
		if arg == "tuto":
			text = ("Le deplacement de la grille ce fait avec les fleches du clavier.\nAstuces : 'R' retoune au dernier mouvement\n Bon jeu!!")
		if arg == "end":
			# Popup de fin de partie
			text = "Plus de déplacements possible réesayer ?"
		self.dial = QtWidgets.QDialog(self)
		self.dial.setGeometry(QtCore.QRect(430, 350, 500, 150))
		label = QtWidgets.QLabel(self.dial)
		label.setText(text)
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		label.setFont(font)
		self.dial.setWindowModality(True)
		self.dial.show()

	def genGrid(self, arg="defaut"):
		# Genere un tableau de cases
		# Chaques cases == (QWidget, tulpe(pos x, pos y), str(valeurCase)) 
		y = 0

		for i in self.grille:
			x = 0
			row = []
			for j in i:
				case = (j, (y, x), j.text())
				row.append(case)
				x+=1
			self.grid.append(row)
			y+=1

	def randNum(self):
		# Une case libre au hasar vaut 2
		search = True
		over = self.over()

		while search and over:
			y = self.grid[randint(0,3)]
			case = y[randint(0,3)]
			case = case[0]
			if self.overOne(case) == True:
				case.setText('2')
				case.setStyleSheet("background-color:{};".format(self.hexa("2")))
				search = False
			else:
				search = True

		if not over:
			print('c\'est plein')
			
			self.popup()
	def over(self):
		# Verifie si au moin une case est vide
		# vide=True,  plein=False
		over = False

		for i in self.grid:
				for j in i:
					if j[0].text() == "":
						over = True
						print('encor de la place')
						break
				if over:
					break

		return over

	def overOne(self, case):
		# verifie case precise 
		# vide=True, plein=False
		over = False 

		if case.text() == "":
			over = True

		return over

	def cut(self, lst):
		# suprime les valeur NULL
		lstGen = []

		for i in lst:
			lstRow = []
			for j in i:
				if j != '':
					lstRow.append(j)
			lstGen.append(lstRow)
		return lstGen

	def uncut(self, lst, axe=1):
		# reconstrui tableau avec valeur NULL
		for i in lst:
			a = 4 - len(i)
			if axe == 1:
				for j in range(a):
					i.insert(0, '')
			if axe == 2:

				for j in range(a):
					i.append('')
		return lst

	def hexa(self, val):
		# retourne couleur/valeur de case
		couleur = [
			("", "#ffffde"),
			("2", "#fad994"),
			("4", "#faa94c"),
			("8", "#ff6762"),
			("16", "#18ff00"),
			("32", "#e2ff00"),
			("64", "#7382ff"), 
			("128", "#db823c"),
			("256","#ff0000"),
			("512","#dbb8b7"),
			("1024","#db00b7"),
			("2048","#2600b3")]
		hexa = ""

		for i in couleur:
			if val == i[0]:
				hexa = i[1]
				break
		return hexa

	def potDeCornichons(self, lst=None, arg='out'):#potDeCornichon definie avec pickle mais incompatible 
		# Enregistre et distribu etat du tableau
		if arg == 'in':
			array = marshal.dump(lst, open('etat.sav', 'wb'))

		if arg == 'out':
			array = marshal.load(open('etat.sav', 'rb'))
			return array

	""" Déplacements du tableau"""
	def move(self, arg):
		array = self.lstIO()

		if arg == "right":
			val = self.cut(array)
			val = self.compte(val, 1)
			val = self.uncut(val, 1)

		if arg == "left":
			val = self.cut(array)
			val = self.compte(val, 2)
			val = self.uncut(val, 2)

		if arg == 'down':
			val = self.rowToCol(array)
			val = self.cut(val)
			val = self.compte(val, 1)
			val = self.uncut(val, 1)
			val = self.rowToCol(val)

		if arg == "up":
			val = self.rowToCol(array)
			val = self.cut(val)
			val = self.compte(val, 2)
			val = self.uncut(val, 2)
			val = self.rowToCol(val)

		if arg == "return":
			val = self.potDeCornichons()

		for i in range(len(val)):
			rowCase = self.grid[i]
			rowVal = val[i]
			for j in range(len(rowVal)):
				case = rowCase[j]
				count = rowVal[j]
				hexa = self.hexa(str(count))
				case[0].setStyleSheet("background-color:{};".format(hexa))
				case[0].setText(str(count))
				self.Score()

		if arg != 'return':
			self.potDeCornichons(array, 'in')
			if val != self.potDeCornichons():
				self.randNum()
			self.Score()

	def Score(self, plus=""):
		score = 0

		for i in self.grid:
			for j in i:
				if j[0].text() != "":
					plus = int(j[0].text())
					score = score + plus

		self.valScore.setText(str(score))

	def compte(self, val, axe=2):

		for i in val:
			if axe == 2:
				compteur = range(len(i)-1)
			if axe == 1 : 
				compteur = reversed(range(len(i)-1))

			for j in compteur:
				if j < len(i):
					if i[j] == i[j+1]:
						i[j+1]=int(i[j])*2
						i[j] = ''

		val = self.cut(val)
		return val

	def lstIO(self):
		# retoune tableau de valeur
		var = self.grid
		lstO = []

		for i in var:
			lstRow = []

			for j in i:
				lstRow.append(j[0].text())
			lstO.append(lstRow)

		return lstO

	def rowToCol(self, lst):
		# Transforme listes de rangées en liste de colones
		lstGen = []

		for i in range(4):
			lstCol = []

			for j in lst:
				lstCol.append(j[i])
			lstGen.append(lstCol)

		return lstGen

	def keyPressEvent(self, event):

		key = event.key()

		if key== QtCore.Qt.Key_Up:
			self.move("up")

		if key== QtCore.Qt.Key_Down:
			self.move("down")

		if key== QtCore.Qt.Key_Left:
			self.move("left")

		if key== QtCore.Qt.Key_Right:
			self.move("right")

		if event.key() == QtCore.Qt.Key_R:
			self.move("return")

if __name__ == '__main__':
	
	import sys 

	app = QApplication(sys.argv)
	uiMain = MainWindow()
	uiMain.show()
	sys.exit(app.exec_())