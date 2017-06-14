from graphics import *
import math

class Turtle:
	''' Simple turtle graphics class. '''
	direction = math.pi/2

	wc = None
	ppos = pos = None 

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

	def parse (self, term, env, depth=6):
		assert type(term)==str
		if depth <= 0:
			return []

		syn = []
		for s in term:
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
	
def hilbertcurve(depth=3):
	width=max(30, (5*(2**depth)-5))
	win = GraphWin("Hilbert curve", width, width)
	gp = Turtle(win, 0,0)

	tree = LTree()
	env = {'A':"-BF+AFA+FB-", 'B':"+AF-BFB-FA+"}
	syn = tree.parse("-BF+AFA+FB-", env, depth)
	tree.exec(gp, syn)

	win.getMouse()
	win.close()

if __name__ == "__main__":
	hilbertcurve(6)
