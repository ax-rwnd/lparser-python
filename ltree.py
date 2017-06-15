from turtle import Turtle

class LTree:
	''' L-Expression tree'''

	class Sym:
		''' Symbol definitions '''
		class Left:
			rep = '-'
			func = Turtle.left
		class Right:
			rep = '+'
			func = Turtle.right
		class Move:
			rep = 'F'
			func = Turtle.move

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
		for func in syn:
			func(turtle)
