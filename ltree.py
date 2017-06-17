from qturtle import QTurtle

class LTree:
	''' L-Expression tree'''

	class Sym:
		''' Symbol definitions '''
		class Left:
			rep = '-'
			func = QTurtle.left
		class Right:
			rep = '+'
			func = QTurtle.right
		class Move:
			rep = 'F'
			func = QTurtle.move
		class Store:
			rep = '['
			func = QTurtle.store
		class Recall:
			rep = ']'
			func = QTurtle.recall

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
			elif (s==self.Sym.Store.rep):
				syn += [self.Sym.Store.func]
			elif (s==self.Sym.Recall.rep):
				syn += [self.Sym.Recall.func]
			else:
				if not s in env:
					raise ValueError("Undefined variable '"+s+"'!")
				else:
					syn += self.parse(env[s], env, depth-1)
		return syn
	
	def exec(self, turtle, syn):
		''' Execute a parsed term '''
		for func in syn:
			func(turtle)
