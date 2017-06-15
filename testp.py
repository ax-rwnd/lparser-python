from lwindow import LWindow

def hilbertcurve(depth, scale=1):
	''' Renders a hilbert curve of given depth '''
	with LWindow("Hilbert Curve", width, width):
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
