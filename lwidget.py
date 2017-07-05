
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QFrame
from PyQt5.QtGui import QPainter, QColor, QPen, QPicture
from PyQt5.QtCore import Qt, QPoint

from qturtle import QTurtle
from ltree import LTree

import math

class LWidget(QFrame):
	''' L-Tree curve rendering widget '''
	axiom = None 
	env = None
	depth = None
	scale = 1
	xpos = 0
	ypos = 0
	delta = 0
	picture = None

	def __init__(self):
		super().__init__()
		self.axiom = ""
		self.env = dict()
		self.depth = 5
		self.initUI()

	def initUI(self):
		self.setStyleSheet("background:white; border:1px solid rgb(50, 50, 50); ")
		self.setMinimumSize(200,200)

	def renderSystem(self):
		self.picture = QPicture()
		qp = QPainter()

		# these offsets don't make sense anymore
		self.xpos = 0
		self.ypos = 0

		qp.begin(self.picture)
		self.rendercurve(qp)
		qp.end()
		self.repaint()
	
	def paintEvent(self, event):
		if self.picture == None:
			print("Warning: picture not yet rendered")
		else:
			qp = QPainter()
			qp.begin(self)
			qp.drawPicture(self.xpos, self.ypos, self.picture)
			qp.end()

	def mousePressEvent(self, event):
		self.offset = event.pos()
	
	def mouseMoveEvent(self, event):
		newPos = event.pos()
		self.xpos -= self.offset.x()-newPos.x()
		self.ypos -= self.offset.y()-newPos.y()
		self.offset = newPos
	
	def mouseReleaseEvent(self, event):
		self.repaint()

	
	def valueSetEvent(self, event):
		''' Event to update vars, sent from main window. '''
		def degtorad(degs):
			return (degs/360)*2*math.pi

		self.axiom = event['axiom']
		self.depth = event['depth']
		self.scale= event['scale']
		self.delta= degtorad(event['delta'])
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
		#print(self.env)
		self.repaint()

	def rendercurve(self, qp):
		''' Draw curve using a turtle '''
		sz = self.size()
		turt = QTurtle(qp, self.xpos+sz.width()/2, self.ypos+sz.height()/2, d=self.delta, speed=self.scale)
		tree = LTree()
		try:
			syn = tree.parse(self.axiom, self.env, self.depth)
		except ValueError as e:
			print("ERROR: "+str(e)+" rendering terminated!")
			return

		tree.exec(turt,syn)
	
if __name__ == "__main__":
	app = QApplication(sys.argv)
	render = LWidget()
	sys.exit(app.exec_())

