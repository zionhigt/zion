from _2048 import Ui_MainWindow

from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import  QtCore

from numpy import array
from random import randint

import sys
import marshal


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):

        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.grid = self.generate_grid()
        self.popup("tuto")
        self.fill_random_case()
        self.compute_score()

    def popup(self, arg="end"):
        if arg == "tuto":
            text = ("Le déplacement de la grille se fait avec les flêches\ndu clavier.\nAstuce : entrez 'r' pour retouner au dernier mouvement\nBon jeu!!")
        if arg == "end":
            # Popup de fin de partie
            text = "Plus de déplacements possible réesayer ?"
        self.show_in_popup(text)

    def fill_random_case(self):
        # Une case libre au hasar vaut 2
        search = True
        over = self.over()

        while search and over:
            rand_row = self.grid[randint(0, 3)]
            case = rand_row[randint(0, 3)]
            case = case[0]
            if self.over_one(case) == True:
                case.setText('2')
                case.setStyleSheet(
                    "background-color:{};".format(self.hexa("2")))
                search = False
            else:
                search = True

        if not over:
            print('c\'est plein')

            self.popup()

    def over(self):
        # Verifie si au moin une case est vide
        # vide=True,  plein=False
        over_list = [j for i in self.grid for j in i if self.over_one(j[0])]
        print(over_list)
        return bool(len(over_list))

    def over_one(self, case):
        # verifie case precise
        # vide=True, plein=False
        return case.text() == ""

    def cut(self, case_list):
        return [[case for case in row if case != ''] for row in case_list]

    def sumation_row(self, vals, axe=2):
        sliced_values = self.cut(vals)
        for i in sliced_values:
            compteur = range(len(i)-1)
            if axe == 1:
                compteur = reversed(range(len(i)-1))

            for j in compteur:
                if j < len(i):
                    if i[j] == i[j+1]:
                        i[j+1] = int(i[j])*2
                        i[j] = ''

        return self.uncut(self.cut(sliced_values), axe)

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
        colors = {
            "0": "#ffffde",
            "2": "#fad994",
            "4": "#faa94c",
            "8": "#ff6762",
            "16": "#18ff00",
            "32": "#e2ff00",
            "64": "#7382ff",
            "128": "#db823c",
            "256": "#ff0000",
            "512": "#dbb8b7",
            "1024": "#db00b7",
            "2048": "#2600b3"
        }

        if val == "":
            val = "0"

        hexa = colors[val]
        return hexa

    def pickles_jar(self, lst=None, arg='out'):
        # Enregistre et distribu etat du tableau
        if arg == 'in':
            array = marshal.dump(lst, open('etat.sav', 'wb'))

        if arg == 'out':
            array = marshal.load(open('etat.sav', 'rb'))
            return array

    def get_grid_values(self):
        return [[case[0].text() for case in row] for row in self.grid]

    def move(self, arg):
        array = self.get_grid_values()

        if arg in ["right", "left"]:
            axis = 1
            if arg == "left":
                axis = 2
            val = self.sumation_row(array, axis)

        if arg in ["down", "up"]:
            val = self.row_to_col(array)
            axis = 1
            if arg == "up":
                axis = 2
            val = self.sumation_row(val, axis)
            val = self.row_to_col(val)

        if arg == "return":
            val = self.pickles_jar()

        for i in range(len(val)):
            for j in range(len(val[i])):
                self.set_case_style(self.grid[i][j], val[i][j])
                self.compute_score()

        if arg != 'return':
            self.pickles_jar(array, 'in')
            if val != self.pickles_jar():
                self.fill_random_case()
            self.compute_score()

    def set_case_style(self, case, count):
        hexa = self.hexa(str(count))
        case[0].setStyleSheet("background-color:{};".format(hexa))
        case[0].setText(str(count))

    def compute_score(self):	
        score = sum([
			int(case) for row in self.get_grid_values()
			for case in row if case != ""
			])
        self.valScore.setText(str(score))

    def row_to_col(self, lst):
        # Transforme listes de rangées en liste de colones
        np_list = array([array(row) for row in lst])
        return np_list.transpose().tolist()

    def keyPressEvent(self, event):

        key = event.key()

        if key == QtCore.Qt.Key_Up:
            self.move("up")

        if key == QtCore.Qt.Key_Down:
            self.move("down")

        if key == QtCore.Qt.Key_Left:
            self.move("left")

        if key == QtCore.Qt.Key_Right:
            self.move("right")

        if event.key() == QtCore.Qt.Key_R:
            self.move("return")


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    uiMain = MainWindow()
    uiMain.show()
    sys.exit(app.exec_())
