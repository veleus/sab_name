from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (
    QTableWidgetItem, 
    QStackedWidget
)
import nail
import hair
import spa
import sys
import db
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

class Db_load(QtWidgets.QMainWindow,db.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.load_accidents)
        self.del_qwe.clicked.connect(self.delete_accident)

    def establish_connection(self):
        connection = sqlite3.connect(r"C:\Users\lovea\OneDrive\Документы\sabrina\salon.db")
        cursor = connection.cursor()
        return connection, cursor

    def load_accidents(self):
        connection, cursor = self.establish_connection()
        cursor.execute('SELECT * FROM "Zapisi"')
        rows = cursor.fetchall()
        column_names = [i[0] for i in cursor.description]
        self.display_table_data(column_names, rows)
        connection.close()

    def display_table_data(self, column_names, rows):
        self.tableWidget.setColumnCount(len(column_names))
        self.tableWidget.setRowCount(len(rows) + 1)
        for i, name in enumerate(column_names):
            item = QTableWidgetItem(name)
            self.tableWidget.setItem(0, i, item)
        for i, row in enumerate(rows):
            for j, col in enumerate(row):
                item = QTableWidgetItem(str(col))
                self.tableWidget.setItem(i + 1, j, item)

    def delete_accident(self):
        accident_id = self.lineEdit.text()
        connection, cursor = self.establish_connection()
        cursor.execute("DELETE FROM Zapisi WHERE id = ?", (accident_id,))
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
        self.load_db = Db_load()


        self.stacked_widget.addWidget(self.example)
        self.stacked_widget.addWidget(self.accidents)
        self.stacked_widget.addWidget(self.spa)
        self.stacked_widget.addWidget(self.load_db)
   


        self.spa.nails.clicked.connect(self.show_spa)
        self.spa.hair.clicked.connect(self.show_spa_hair)
        self.spa.pushButton_4.clicked.connect(self.show_db)


        self.example.spa.clicked.connect(self.show_spa_example)
        self.example.nails.clicked.connect(self.show_accidents)
        self.example.pushButton_4.clicked.connect(self.show_db_example)

        self.accidents.spa.clicked.connect(self.show_spa_accinets)
        self.accidents.hair.clicked.connect(self.show_example)
        self.accidents.pushButton_4.clicked.connect(self.show_db_accidents)

        self.load_db.spa.clicked.connect(self.show_spa_from)
        self.load_db.hair.clicked.connect(self.show_hair_from)
        self.load_db.nails.clicked.connect(self.show_nails_from)


    def show_example(self):
        self.stacked_widget.setCurrentWidget(self.example)
    def show_spa_accinets(self):
        self.stacked_widget.setCurrentWidget(self.spa)
    def show_db_accidents(self):
        self.stacked_widget.setCurrentWidget(self.load_db)

    def show_db_example(self):
        self.stacked_widget.setCurrentWidget(self.load_db)
    def show_spa_example(self):
        self.stacked_widget.setCurrentWidget(self.spa)
    def show_accidents(self):
        self.stacked_widget.setCurrentWidget(self.accidents)
    
    def show_db(self):
        self.stacked_widget.setCurrentWidget(self.load_db)
    def show_spa_hair(self):
        self.stacked_widget.setCurrentWidget(self.example)
    def show_spa(self):
        self.stacked_widget.setCurrentWidget(self.accidents)

    def show_spa_from(self):
        self.stacked_widget.setCurrentWidget(self.spa)
    def show_hair_from(self):
        self.stacked_widget.setCurrentWidget(self.example)
    def show_nails_from(self):
        self.stacked_widget.setCurrentWidget(self.accidents)
    
    

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())