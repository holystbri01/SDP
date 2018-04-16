import sys
import os
import datetime
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import uic
from SDPCode1 import *

class MyMainWindow(QMainWindow):
	def __init__(self):
		super(QMainWindow, self).__init__()
		self.chain = Chain()
		self.chain.addBlock(item)

		self.setFixedSize(1200,700)
		self.setWindowIcon(QIcon("comcast logo.png"))
		self.setWindowTitle("SDP Team 3")
		self.setStyleSheet("background-image: url(base background.png) center no-repeat;")

		self.mainwidget = QWidget()
		self.vbox = QVBoxLayout(self.mainwidget)
		self.vbox.setSpacing(13)
		
		butts = ArmingButton()
		butts.setGeometry(QRect(0,0,483,40))
		self.vbox.addWidget(butts,0, Qt.AlignLeft)
		self.widge = gridlayout()
		self.widge.setGeometry(QRect(0,0, 1200, 500))

		self.widge.button3.clicked.connect(self.add_device)
		self.widge.button5.clicked.connect(self.log)
		
		self.vbox.addWidget(self.widge,0, Qt.AlignCenter)
		#(left, top, bottom, right)
		self.vbox.setContentsMargins(10,40,10,80)

		self.setCentralWidget(self.mainwidget)

### Functions to handle click events for each button
### Add attributes to ListWindow to tell it what to display line-by-line

	def log(self):
		window = ListWindow("Log")
		window.show()
		self.window = window

#	def current_devices(self):
#		window = ListWindow("Current Devices")
#		window.show()

#	def remove_device(self):
#		window = ListWindow("Remove a Device")
#		window.show()
	
#	def thermostats(self):
#		window = ListWindow("Thermostats")
#		window.show()


### Need popup dialog windows to accept user input
	def add_device(self):
		pop_up = addWindow("Add a Device")
		pop_up.show()
		self.pop_up = pop_up

#	def settings(self):
#		pass

class gridlayout(QWidget):
	def __init__(self):
		super(QWidget, self).__init__()
#labels
		self.label1 = ImageLabel(QPixmap("current devices button.png"))

		self.label2 = ImageLabel(QPixmap("add device button.png"))

		self.label3 = ImageLabel(QPixmap("remove device button.png"))

		self.label4 = ImageLabel(QPixmap("thermostats button.png"))

		self.label5 = ImageLabel(QPixmap("security log button.png"))

		self.label6 = ImageLabel(QPixmap("settings button.png"))

#buttons
		self.button1 = ImageButton(QPixmap("devices current icon.png"))

		self.button2 = ImageButton(QPixmap("add button.png"))

		self.button3 = ImageButton(QPixmap("remove button.png"))

		self.button4 = ImageButton(QPixmap("thermostat button.png"))

		self.button5 = ImageButton(QPixmap("view log button.png"))

		self.button6 = ImageButton(QPixmap("settings icon.png"))


#setup of grid, putting buttons in gridlayout
		qgrid = QGridLayout(self)
		qgrid.setHorizontalSpacing(80)

		qgrid.addWidget(self.button1, 0, 0, 2, 1, Qt.AlignCenter)
		qgrid.addWidget(self.button2, 0, 3, 2, 1, Qt.AlignCenter)
		qgrid.addWidget(self.button3, 0, 5, 2, 1, Qt.AlignCenter)

		qgrid.addWidget(self.label1, 2, 0, 1, 1)
		qgrid.addWidget(self.label2, 2, 3, 1, 1)
		qgrid.addWidget(self.label3, 2, 5, 1, 1)

		qgrid.addWidget(self.button4, 4, 0, 2, 1, Qt.AlignCenter)
		qgrid.addWidget(self.button5, 4, 3, 2, 1, Qt.AlignCenter)
		qgrid.addWidget(self.button6, 4, 5, 2, 1, Qt.AlignCenter)

		qgrid.addWidget(self.label4, 6, 0, 1, 1)
		qgrid.addWidget(self.label5, 6, 3, 1, 1)
		qgrid.addWidget(self.label6, 6, 5, 1, 1)


class ListWindow(QPlainTextEdit):
	def __init__(self, title):
		super(QPlainTextEdit, self).__init__()
		self.setReadOnly(True)
		self.setWindowIcon(QIcon("comcast logo.png"))
		self.setWindowTitle(title)
		self.setStyleSheet("background-color: gray;")

		self.time = datetime.datetime.now().strftime('%c')
		self.insertPlainText(QString(self.time))

class addWindow(QWidget):
	def __init__(self, title):
		super(QWidget, self).__init__()
		self.setWindowIcon(QIcon("comcast logo.png"))
		self.setWindowTitle(title)

		form = QFormLayout()

		line1 = QLineEdit()
		line1.setAlignment(Qt.AlignRight)
		line1.setFont(QFont("Times New Roman", 14))

		line2 = QLineEdit()
		line2.setAlignment(Qt.AlignRight)
		line2.setFont(QFont("Times New Roman", 14))

		line3 = QLineEdit()
		line3.setAlignment(Qt.AlignRight)
		line3.setFont(QFont("Times New Roman", 14))


		form.addRow("Device Name",line1)
		form.addRow("Device Type", line2)
		form.addRow("Device Address", line3)
					
		self.addLayout(form)
		

class ImageLabel(QAbstractButton):
	def __init__(self, pixmap):
		super(QAbstractButton, self).__init__()
		self.pixmap=pixmap.scaled(287,80)

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
	def __init__(self):
		super(QAbstractButton, self).__init__()
		self.armed = False
		self.pixmap = QPixmap("disarmed button.png")
		self.pixmap=self.pixmap.scaled(483,30)
		self.clicked.connect(self.arming)

	def arming(self):
		if self.armed == False:
			self.armed = True
			self.pixmap = QPixmap("armed button.png")
		else:
			self.armed = False
			self.pixmap = QPixmap("disarmed button.png")
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
