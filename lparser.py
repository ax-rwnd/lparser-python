from graphics import *
import math

class Turtle:
	''' Simple turtle graphics class. '''
	direction = math.pi/2

	wc = None
	ppos = pos = None 
	
	"""
	Debug purposes
	minx = 65563
	maxx = -65563
	miny = 65563
	maxy = -65563
	"""

	def __init__(self, wc, x, y):
		self.ppos = self.pos = Point(x,y)
		self.wc = wc

	def turn(self, delta):
		self.direction += delta

	def move(self, dist, adraw=True):
		''' Move with respect to direction, drawing is optional'''
		self.ppos = self.pos
		self.pos = Point(self.ppos.x+dist*math.cos(self.direction),
				self.ppos.y+dist*math.sin(self.direction))
		if adraw:
			self.draw()

	def draw(self):
		''' Print a line between this and the previous pos'''
		line = Line(self.ppos, self.pos)
		line.draw(self.wc)

		"""
		Debug purposes
		if self.minx > self.pos.x:
			self.minx = self.pos.x
		if self.maxx < self.pos.x:
			self.maxx = self.pos.x
		if self.miny > self.pos.y:
			self.miny = self.pos.y
		if self.maxy < self.pos.y:
			self.maxy = self.pos.y
		"""

	def mark(self, d):
		''' Mark a circle around the turtle'''
		circle = Circle(self.pos, d)
		circle.draw(self.wc)

class LTree:
	''' L-Expression tree'''

	class Sym:
		''' Symbol definitions '''
		class Left:
			rep = '-'
			func = (Turtle.turn, -(math.pi/2))
		class Right:
			rep = '+'
			func = (Turtle.turn, math.pi/2)
		class Move:
			rep = 'F'
			func = (Turtle.move, 5)

	def parse (self, axiom, env, depth):
		assert type(axiom)==str
		if depth <= 0:
			return []

		syn = []
		for s in axiom:
			if (s==self.Sym.Left.rep):
				syn += [self.Sym.Left.func]
			elif (s==self.Sym.Right.rep):
				syn += [self.Sym.Right.func]
			elif (s==self.Sym.Move.rep):
				syn += [self.Sym.Move.func]
			else:
				assert s in env #error: undefined var
				syn += self.parse(env[s], env, depth-1)
		return syn
	
	def exec(self, turtle, syn):
		''' Execute a parsed term '''
		for func, arg in syn:
			func(turtle, arg)
	
def hilbertcurve(depth):
	''' Renders a hilbert curve of given depth '''
	width=max(30, (5*(2**depth)-5))
	win = GraphWin("Hilbert curve", width, width)
	gp = Turtle(win, 0,0)

	# parse l-system using alphabet and axiom
	tree = LTree()
	env = {'A':"-BF+AFA+FB-", 'B':"+AF-BFB-FA+"}
	axiom = "-BF+AFA+FB-"
	syn = tree.parse(axiom, env, depth)

	# render tree
	tree.exec(gp, syn)

	win.getMouse()
	win.close()

def kochcurve(depth):
	''' Renders a koch curve of order depth '''
	def calcheight (depth):
		if depth<=1:
			return 0
		else:
			return 15*(3**(depth-3))+calcheight(depth-1)
	height = max(30, calcheight(depth))
	width = max(30, 5*(3**(depth-1)))
	win = GraphWin("Koch curve", width, height)
	gp = Turtle(win, width,height)
	gp.direction = math.pi

	tree = LTree()
	env = {'A':"A+FA-FA-FA+FA"}
	axiom = 'FA'
	syn = tree.parse(axiom, env, depth)

	# render tree
	tree.exec(gp, syn)

	#print("X1:{} X2:{} Y1:{} Y2:{}".format(gp.minx,gp.maxx,gp.miny,gp.maxy))

	win.getMouse()
	win.close()

if __name__ == "__main__":
	kochcurve(5)
