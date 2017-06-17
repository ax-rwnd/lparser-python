
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QFrame
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt

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
		''' Event to update vars, sent from main window. '''
		def degtorad(degs):
			return (degs/360)*2*math.pi

		self.axiom = event['axiom']
		self.depth = event['depth']
		self.scale= event['scale']
		self.xpos = event['xpos']
		self.ypos = event['ypos']
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
		print(self.env)
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

