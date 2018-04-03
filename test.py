import sys
import os
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class Window(QWidget):

	def __init__(self):
### initialize the Window widget (referencing QWidget as superclass)
		super(QWidget,self).__init__()
#		win = QWidget()
		self.label = QLabel()

		self.label.setPixmap(QPixmap("base background.png"))

		self.vbox = QVBoxLayout()
		self.vbox.addWidget(self.label)

		self.setLayout(self.vbox)
		self.setWindowTitle("SDP Team 3")
		self.setWindowIcon(QIcon("emblem-comcast-png-logo-6.png"))

#		self.hbox = QHBoxLayout(self)
#### 		will need to use this as the "horizontal layout and addlayout() to widget
#		button = ImageButton(QPixmap("", self))


#		self.show()
	

	def close_app(self):
		sys.exit()	

class ImageButton(QAbstractButton):
	def __init__(self, pixmap, parent = None):
		super(ImageButton, self).__init__(parent)
		self.pixmap = pixmap

	def paintEvent (self, event):
		painter = QPainter(self)
		painter.drawPixmap(event.rect(), self.pixmap)

	def sizeHint(self):
		return self.pixmap.size()
	
def main():
	app = QApplication(sys.argv)
	GUI = Window()
	GUI.show()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()
