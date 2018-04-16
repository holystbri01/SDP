import sys
import os
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import uic

class MyMainWindow(QMainWindow):
	def __init__(self):
		super(QMainWindow, self).__init__()
		self.setGeometry(QRect(100,100,1200,700))
		self.setWindowIcon(QIcon("comcast logo.png"))
		self.setStyleSheet("background-image: url(base background.png) center no-repeat;")

		self.mainwidget = QWidget()
		self.vbox = QVBoxLayout(self.mainwidget)
		self.vbox.setSpacing(13)
		
		butts = ArmingButton(QPixmap("disarmed button.png"))
		butts.setGeometry(QRect(0,0,483,40))
		self.vbox.addWidget(butts,0, Qt.AlignLeft)
		self.widge = gridlayout()
		self.widge.setGeometry(QRect(0,0, 1200, 500))
		self.vbox.addWidget(self.widge,0, Qt.AlignCenter)
		#(left, top, bottom, right)
		self.vbox.setContentsMargins(10,40,10,225)

		self.setCentralWidget(self.mainwidget)

class gridlayout(QWidget):
	def __init__(self):
		super(QWidget, self).__init__()

#labels
		label1 = ImageLabel(QPixmap("current devices button.png"))
		label2 = ImageLabel(QPixmap("add device button.png"))
		label3 = ImageLabel(QPixmap("remove device button.png"))
		label4 = ImageLabel(QPixmap("thermostats button.png"))
		label5 = ImageLabel(QPixmap("security log button.png"))
		label6 = ImageLabel(QPixmap("settings button.png"))
#buttons
		button1 = ImageButton(QPixmap("devices current icon.png"))
		button2 = ImageButton(QPixmap("add button.png"))
		button3 = ImageButton(QPixmap("remove button.png"))
		button4 = ImageButton(QPixmap("thermostat button.png"))
		button5 = ImageButton(QPixmap("view log button.png"))
		button6 = ImageButton(QPixmap("settings icon.png"))

#setup
		qgrid = QGridLayout(self)
		qgrid.setHorizontalSpacing(80)

		qgrid.addWidget(button1, 0, 0, 2, 1, Qt.AlignCenter)
		qgrid.addWidget(button2, 0, 3, 2, 1, Qt.AlignCenter)
		qgrid.addWidget(button3, 0, 5, 2, 1, Qt.AlignCenter)

		qgrid.addWidget(label1, 2, 0, 1, 1)
		qgrid.addWidget(label2, 2, 3, 1, 1)
		qgrid.addWidget(label3, 2, 5, 1, 1)

		qgrid.addWidget(button4, 4, 0, 2, 1, Qt.AlignCenter)
		qgrid.addWidget(button5, 4, 3, 2, 1, Qt.AlignCenter)
		qgrid.addWidget(button6, 4, 5, 2, 1, Qt.AlignCenter)

		qgrid.addWidget(label4, 6, 0, 1, 1)
		qgrid.addWidget(label5, 6, 3, 1, 1)
		qgrid.addWidget(label6, 6, 5, 1, 1)

class ImageLabel(QAbstractButton):
	def __init__(self, pixmap):
		super(QAbstractButton, self).__init__()
		self.pixmap=pixmap.scaled(287,90)

	def paintEvent(self, event):
		painter = QPainter(self)
		painter.drawPixmap(event.rect(), self.pixmap)
	def sizeHint(self):
		return self.pixmap.size()

class ImageButton(QAbstractButton):
	def __init__(self, pixmap):
		super(QAbstractButton, self).__init__()
		self.pixmap=pixmap.scaled(202,202)

	def paintEvent(self, event):
		painter = QPainter(self)
		painter.drawPixmap(event.rect(), self.pixmap)
	def sizeHint(self):
		return self.pixmap.size()

class ArmingButton(QAbstractButton):
	def __init__(self, pixmap):
		super(QAbstractButton, self).__init__()
		self.pixmap=pixmap.scaled(483,30)
		self.armed = False

	def paintEvent(self, event):
		painter = QPainter(self)
		painter.drawPixmap(event.rect(), self.pixmap)
	def sizeHint(self):
		return self.pixmap.size()

def main():
	app = QApplication(sys.argv)
	GUI = MyMainWindow()
	GUI.show()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()
