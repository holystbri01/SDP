import sys
import os
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class gridlayout(QWidget):
	def __init__(self):
		super(QWidget, self).__init__()

		label1 = ImageLabel(QPixmap("current devices button.png"))
		label2 = ImageLabel(QPixmap("add device button.png"))
		label3 = ImageLabel(QPixmap("remove device button.png"))
		label4 = ImageLabel(QPixmap("thermostats button.png"))
		label5 = ImageLabel(QPixmap("security log button.png"))
		label6 = ImageLabel(QPixmap("settings button.png"))
		
		button1 = ImageButton(QPixmap("devices current icon.png"))
		button2 = ImageButton(QPixmap("add button.png"))
		button3 = ImageButton(QPixmap("remove button.png"))
		button4 = ImageButton(QPixmap("thermostat button.png"))
		button5 = ImageButton(QPixmap("view log button.png"))
		button6 = ImageButton(QPixmap("settings icon.png"))

		grid_layout = QGridLayout(self)
	# first row of buttons
		grid_layout.addWidget(button1, 0, 0, 2, 1, Qt.AlignCenter)
		grid_layout.addWidget(button2, 0, 3, 2, 1, Qt.AlignCenter)
		grid_layout.addWidget(button3, 0, 5, 2, 1, Qt.AlignCenter)
	#first row of labels
		grid_layout.addWidget(label1, 2, 0, 1, 2)
	#attempting to fix spacing issue (labels)
#		grid_layout.setVerticalSpacing(5)
		grid_layout.addWidget(label2, 2, 3, 1, 2)
		grid_layout.addWidget(label3, 2, 5, 1, 2)
	#second row of buttons
		grid_layout.addWidget(button4, 4, 0, 2, 1, Qt.AlignCenter)
		grid_layout.addWidget(button5, 4, 3, 2, 1, Qt.AlignCenter)
		grid_layout.addWidget(button6, 4, 5, 2, 1, Qt.AlignCenter)
	#second row of labels
		grid_layout.addWidget(label4, 6, 0, 1, 1)
		grid_layout.addWidget(label5, 6, 3, 1, 1)
		grid_layout.addWidget(label6, 6, 5, 1, 1)

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
		self.pixmap=pixmap.scaled(422,155)

	def paintEvent(self, event):
		painter = QPainter(self)
		painter.drawPixmap(event.rect(), self.pixmap)
	def sizeHint(self):
		return self.pixmap.size()


def main():
	app = QApplication(sys.argv)
	ui = gridlayout()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()

