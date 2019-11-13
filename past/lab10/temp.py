import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QPushButton,
                                QLineEdit, QHBoxLayout, QVBoxLayout, QComboBox)
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QColor

my_list = ["Pick a color", "vermillon", "salmon", "khaki", "plum"]
my_RGBdata = ["", "(227, 66, 52)", "(250, 128, 114)", "(240,230,140)", "(221, 160, 221)"]
my_HEXdata = ["", "#e34234", "#fa8072", "#f0e78c", "#dda0dd"]


class Window2(QWidget):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Show colors")

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.intro = QLabel('CST 205 Color Exchange!', self)
        self.my_combo_box = QComboBox()
        self.my_combo_box.addItems(my_list)
        self.my_RGB = QLabel('RGB: ', self)
        self.my_HEX = QLabel('Hex: ', self)
        self.my_btn = QPushButton("Show colors")

        hbox = QHBoxLayout()
        hbox.addWidget(self.my_RGB)
        hbox.addWidget(self.my_HEX)

        vbox = QVBoxLayout()
        vbox.addWidget(self.intro)
        vbox.addWidget(self.my_combo_box)
        vbox.addLayout(hbox)
        vbox.addWidget(self.my_btn)


        self.setLayout(vbox)
        self.my_combo_box.currentIndexChanged.connect(self.update_ui1)
        self.my_combo_box.currentIndexChanged.connect(self.update_ui2)
        self.my_btn.clicked.connect(self.Window2)
        self.setWindowTitle("Colors!")


    @pyqtSlot()
    def update_ui1(self):
        my_text = self.my_combo_box.currentText()
        my_index = self.my_combo_box.currentIndex()
        self.my_RGB.setText(f'RGB: {my_RGBdata[my_index]}')

    def update_ui2(self):
        my_text = self.my_combo_box.currentText()
        my_index = self.my_combo_box.currentIndex()
        self.my_HEX.setText(f'HEX: {my_HEXdata[my_index]}')

    def Window2(self):
        i = self.my_combo_box.currentIndex()
        if i != 0:
        	w = self.w = Window2()
	        self.w.show()
	        self.setAutoFillBackground(True)
	        p = w.palette()
	        p.setColor(w.backgroundRole(), QColor(my_RGBdata[i]))
	        w.setPalette(p)



app = QApplication(sys.argv)
main = Window()
main.show()
sys.exit(app.exec_())


