
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QFrame
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt

from qturtle import QTurtle
from ltree import LTree

class LWidget(QFrame):
	axiom = None 
	env = None
	depth = None

	def __init__(self):
		super().__init__()
		self.axiom = ""
		self.env = dict()
		self.depth = 5
		self.initUI()

	def initUI(self):
		self.setStyleSheet("background:white; border:1px solid rgb(50, 50, 50); ")
		self.setMinimumSize(200,200)

	def paintEvent(self, event):
		qp = QPainter()
		qp.begin(self)
		self.rendercurve(qp)
		qp.end()
	
	def valueSetEvent(self, event):
		self.axiom = event['axiom']
		self.env = {}
		assignments = event['env'].split('\n')
		for var in assignments:
			var = var.replace(' ','')
			var = var.replace('\t','')
			try:
				(l,r) = var.split('=',2)
				self.env[l] = r
			except ValueError:
				pass
		print(self.env)
		self.repaint()

	def rendercurve(self, qp):
		sz = self.size()
		turt = QTurtle(qp, sz.width()/2, sz.height()/2)
		tree = LTree()
		syn = tree.parse(self.axiom, self.env, self.depth)
		tree.exec(turt,syn)
	
if __name__ == "__main__":
	app = QApplication(sys.argv)
	render = LWidget()
	sys.exit(app.exec_())

