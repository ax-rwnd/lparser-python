from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import QPoint
import math

class QTurtle():
	direction = 0

	ppos = pos = None
	delta = None
	speed = None
	qp = None

	def __init__(self, qp, x, y, d=math.pi/2, speed=5):
		self.ppos = self.pos = QPoint(x,y)
		self.qp = qp
		self.delta = d
		self.speed = speed

	def left(self):
		self.direction -= self.delta
	def right(self):
		self.direction += self.delta

	def move(self, draw=True):
		self.ppos = self.pos
		nx = self.ppos.x() + self.speed*math.cos(self.direction)
		ny = self.ppos.y() + self.speed*math.sin(self.direction)
		self.pos = QPoint(nx, ny)

		if draw:
			self.draw()

	def draw(self):
		''' Print a line between this and the previous pos'''
		self.qp.drawLine(self.ppos.x(), self.ppos.y(), self.pos.x(), self.pos.y())

