from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (
    QTableWidgetItem, 
    QStackedWidget
)
import nail
import hair
import spa
import sys
import res_rc
import sqlite3

import datetime


class Hair(QtWidgets.QMainWindow, hair.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.zapis_vika.clicked.connect(self.load_accidents)
    def establish_connection(self):
        connection = sqlite3.connect(r"C:\Users\lovea\OneDrive\Документы\sabrina\salon.db")
        cursor = connection.cursor()
        return connection, cursor

    
    def load_accidents(self):

        selected_item = self.vika_combo.currentText()
        print(f"Loading Accidents...{selected_item}")
        connection, cursor = self.establish_connection()
        now = datetime.date.today()
        cursor.execute("INSERT INTO Zapisi (data_sapisi, name) VALUES (?, ?)",
                       (f'{now}:{selected_item}', 'Вика'))
        connection.commit()
        connection.close()


class Nail(QtWidgets.QMainWindow, nail.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.zapis_valeria.clicked.connect(self.load_accidents)
    def establish_connection(self):
        connection = sqlite3.connect(r"C:\Users\lovea\OneDrive\Документы\sabrina\salon.db")
        cursor = connection.cursor()
        return connection, cursor

    
    def load_accidents(self):

        selected_item = self.valeria_combo.currentText()
        print(f"Loading Accidents...{selected_item}")
        connection, cursor = self.establish_connection()
        now = datetime.date.today()
        cursor.execute("INSERT INTO Zapisi (data_sapisi, name) VALUES (?, ?)",
                       (f'{now}:{selected_item}', 'Валерия'))
        connection.commit()
        connection.close()



class Spa(QtWidgets.QMainWindow,spa.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.olga_alina.clicked.connect(self.load_accidents)
    def establish_connection(self):
        connection = sqlite3.connect(r"C:\Users\lovea\OneDrive\Документы\sabrina\salon.db")
        cursor = connection.cursor()
        return connection, cursor

    
    def load_accidents(self):

        selected_item = self.olga_combo.currentText()
        print(f"Loading Accidents...{selected_item}")
        connection, cursor = self.establish_connection()
        now = datetime.date.today()
        cursor.execute("INSERT INTO Zapisi (data_sapisi, name) VALUES (?, ?)",
                       (f'{now}:{selected_item}', 'Ольга'))
        connection.commit()
        connection.close()


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)



        self.example = Hair()
        self.accidents = Nail()
        self.spa = Spa()

        self.stacked_widget.addWidget(self.example)
        self.stacked_widget.addWidget(self.accidents)
        self.stacked_widget.addWidget(self.spa)
    


        self.spa.nails.clicked.connect(self.show_spa)
        self.spa.hair.clicked.connect(self.show_spa_hair)

        self.example.spa.clicked.connect(self.show_spa_example)
        self.example.nails.clicked.connect(self.show_accidents)

        self.accidents.spa.clicked.connect(self.show_spa_accinets)
        self.accidents.hair.clicked.connect(self.show_example)

    def show_example(self):
        self.stacked_widget.setCurrentWidget(self.example)
    def show_spa_accinets(self):
        self.stacked_widget.setCurrentWidget(self.spa)


    def show_spa_example(self):
        self.stacked_widget.setCurrentWidget(self.spa)
    def show_accidents(self):
        self.stacked_widget.setCurrentWidget(self.accidents)
    
    def show_spa_hair(self):
        self.stacked_widget.setCurrentWidget(self.example)
    def show_spa(self):
        self.stacked_widget.setCurrentWidget(self.accidents)

    
    

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())