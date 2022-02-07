import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout
from PyQt5.QtWidgets import QPushButton, QLineEdit, QSizePolicy

class Calculadora(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Calculadora")
        self.setFixedSize(400, 400)
        self.cw = QWidget()
        self.grid = QGridLayout(self.cw)

        self.display = QLineEdit()
        self.grid.addWidget(self.display, 0, 0, 1, 5)
        self.display.setDisabled(True)
        self.setStyleSheet(
            '*{background: #FFF; color: #000; font-size:30px;}'
        )
        self.display.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        self.add_button(QPushButton("7"), 1,0,1,1)

        self.setCentralWidget(self.cw)

    def add_button(self, btn, row, col, rowspan, colspan):
        self.grid.addWidget(btn, row, col,rowspan, colspan)
        btn.clicked.connect(lambda: self.display.setText(
            self.display.text() + btn.text()
        ))

if __name__ == '__main__':
    qt = QApplication(sys.argv)
    calc = Calculadora()
    calc.show()
    qt.exec_()
