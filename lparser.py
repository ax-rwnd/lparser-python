from ltree import LTree
from turtle import Turtle
from graphics import GraphWin
import math
	
def hilbertcurve(depth, scale=1):
	''' Renders a hilbert curve of given depth '''
	width=max(30, (scale*(2**depth)-scale))
	win = GraphWin("Hilbert curve", width, width)
	gp = Turtle(win, 0,0, speed=scale)

	# parse l-system using alphabet and axiom
	tree = LTree()
	env = {'A':"-BF+AFA+FB-", 'B':"+AF-BFB-FA+"}
	axiom = "-BF+AFA+FB-"
	syn = tree.parse(axiom, env, depth)

	# render tree
	tree.exec(gp, syn)

	win.getMouse()
	win.close()

def kochcurve(depth, scale=1):
	''' Renders a koch curve of order depth '''
	def calcheight (depth, scale):
		if depth<=1:
			return 0
		else:
			return (3*scale)*(3**(depth-3))+calcheight(depth-1, scale)
	height = max(30, calcheight(depth, scale))
	width = max(30, scale*(3**(depth-1)))

	win = GraphWin("Koch curve", width, height)
	gp = Turtle(win, width,height, speed=scale)
	gp.direction = math.pi

	tree = LTree()
	env = {'A':"A+FA-FA-FA+FA"}
	axiom = 'FA'
	syn = tree.parse(axiom, env, depth)

	# render tree
	tree.exec(gp, syn)

	win.getMouse()
	win.close()

def sarrowcurve(depth, scale=1):
	''' Sierpinski arrowehead approximation '''
	win = GraphWin("Sieprinski approximation", 400, 400)

	gp = Turtle(win, 200, 200, delta=2*math.pi/6, speed=1)
	gp.direction = math.pi 

	tree = LTree()
	env = {'A':"+FB-FA-FB+", 'B':"-FA+FB+FA-"}
	axiom = "FA"
	syn = tree.parse(axiom, env, depth)
	tree.exec(gp, syn)

	print("X1:{} X2:{} Y1:{} Y2:{}".format(gp.minx,gp.maxx,gp.miny,gp.maxy))
	
	win.getMouse()
	win.close()

def workbench(depth, scale=1):
	win = GraphWin("Workbench", 400, 400)

	gp = Turtle(win, 200, 200, delta=2*math.pi/4, speed=scale)
	gp.direction = math.pi 

	tree = LTree()
	env = {'E':"FE+FEFE-FEFE-FE-FE+FE+FEFE-FE-FE+FE+FEFE+FEFE-FE"}
	axiom = "FE-FE-FE-FE"
	syn = tree.parse(axiom, env, depth)
	tree.exec(gp, syn)
	
	win.getMouse()
	win.close()

	"""
	Additional koch curve
	env = {'E':"FEFE-FE-FE-FE-FEFE"}
	axiom = "FE-FE-FE-FE"

	env = {'E':"FEFE-FE-FE-FE-FE-FE+FE"}
	axiom = "FE-FE-FE-FE"


	Koch island
	env = {'E':"FE+FEFE-FEFE-FE-FE+FE+FEFE-FE-FE+FE+FEFE+FEFE-FE"}
	axiom = "FE-FE-FE-FE"
	"""

if __name__ == "__main__":
	workbench(4, scale=1)
