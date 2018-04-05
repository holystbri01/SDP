import sys
import os
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class gridlayout(QWidget):
	def __init__(self):
		super(QWidget, self).__init__()

		lab1 = QLabel("Label1")
		line_edit1 = QLineEdit()
		sub1 = QVBoxLayout()
		sub1.addWidget(lab1)
		sub1.addWidget(line_edit1)

		lab2 = QLabel("Label2")
		line_edit2 = QLineEdit()
		sub2 = QVBoxLayout()
		sub2.addWidget(lab2)
		sub2.addWidget(line_edit2)

		button1 = ImageButton(QPixmap("devices current icon.png"))
		button2 = ImageButton(QPixmap("add button.png"))
		button3 = ImageButton(QPixmap("remove button.png"))
		button4 = ImageButton(QPixmap("thermostat button.png"))
		button5 = ImageButton(QPixmap("view log button.png"))

		grid_layout = QGridLayout(self)
		grid_layout.addLayout(sub1, 0, 0, 1, 3)
		grid_layout.addLayout(sub2, 1, 0, 1, 3)
		grid_layout.addWidget(button1, 2, 0, 1, 1)
		grid_layout.addWidget(button2, 2, 1, 1, 1)
		grid_layout.addWidget(button3, 2, 2, 1, 1)
		grid_layout.addWidget(button4, 3, 0, 1, 1)
		grid_layout.addWidget(button5, 3, 1, 1, 1)

		self.show()

class ImageButton(QAbstractButton):
	def __init__(self, pixmap):
		super(QAbstractButton, self).__init__()
		self.pixmap=pixmap.scaled(225,225)

	def paintEvent(self,event):
		painter = QPainter(self)
		painter.drawPixmap(event.rect(), self.pixmap)

	def sizeHint(self):
		return self.pixmap.size()

class ImageLabel(QLabel):
	def __init__(self,pixmap):
		super(QLabel, self).__init__()
		self.pixmap=pixmap
		self.setPixmap(pixmap)


def main():
	app = QApplication(sys.argv)
	ui = gridlayout()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()

