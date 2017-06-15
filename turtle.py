from graphics import Point, Line
import math

class Turtle:
	''' Simple turtle graphics class. '''
	direction = math.pi/2

	delta = None
	speed = None

	wc = None
	ppos = pos = None 
	
	"""
	Debug purposes
	"""
	minx = 65563
	maxx = -65563
	miny = 65563
	maxy = -65563

	def __init__(self, wc, x, y, delta=math.pi/2, speed=5):
		self.ppos = self.pos = Point(x,y)
		self.wc = wc
		self.delta = delta
		self.speed = speed

	def left(self):
		self.direction -= self.delta
	def right(self):
		self.direction += self.delta
	def turn(self, delta):
		self.direction += delta

	def move(self, adraw=True):
		''' Move with respect to direction, drawing is optional'''
		self.ppos = self.pos
		self.pos = Point(self.ppos.x+self.speed*math.cos(self.direction),
				self.ppos.y+self.speed*math.sin(self.direction))
		if adraw:
			self.draw()

	def draw(self):
		''' Print a line between this and the previous pos'''
		line = Line(self.ppos, self.pos)
		line.draw(self.wc)

		"""
		Debug purposes
		"""
		if self.minx > self.pos.x:
			self.minx = self.pos.x
		if self.maxx < self.pos.x:
			self.maxx = self.pos.x
		if self.miny > self.pos.y:
			self.miny = self.pos.y
		if self.maxy < self.pos.y:
			self.maxy = self.pos.y

	def mark(self, d):
		''' Mark a circle around the turtle'''
		circle = Circle(self.pos, d)
		circle.draw(self.wc)

