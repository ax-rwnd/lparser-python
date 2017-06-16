#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp, QLineEdit, QLabel, QWidget, QPlainTextEdit, QPushButton, QVBoxLayout,QGridLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

from lwidget import LWidget

class LParseQT(QMainWindow):
	def __init__(self):
		super().__init__()
		self.windowsetup()

	bsubmit = None
	aedit = None
	vedit = None
	lrender = None
	mainwidget = None

	def toolbarsetup(self):
		exitAction = QAction(QIcon('render.png'), 'Render', self)
		exitAction.setShortcut('Ctrl+R')
		exitAction.triggered.connect(self.signalRender)

		self.toolbar = self.addToolBar('Exit')
		self.toolbar.addAction(exitAction)

	def layoutsetup(self):
		self.mainwidget = QWidget(self)
		self.setCentralWidget(self.mainwidget)

		vbox = QVBoxLayout()
		self.lrender = LWidget()

		vargrid = QGridLayout()
		alabel = QLabel("Axiom")
		vargrid.addWidget(alabel,0,0)
		self.aedit = QLineEdit()
		vargrid.addWidget(self.aedit,0,1)

		vlabel = QLabel("Variables")
		vargrid.addWidget(vlabel,1,0)
		self.vedit = QPlainTextEdit()
		vargrid.addWidget(self.vedit,1,1)

		# Actual layout
		vbox.addWidget(self.lrender,1)
		vbox.addLayout(vargrid)
		self.mainwidget.setLayout(vbox)

	def windowsetup(self):
		self.toolbarsetup()
		self.layoutsetup()

		self.setWindowTitle("L-Parser")
		self.show()

	def signalRender(self):
		self.lrender.valueSetEvent({"axiom":self.aedit.text(), "env":self.vedit.toPlainText()})

if __name__ == "__main__":
	app = QApplication(sys.argv)
	render = LParseQT()
	sys.exit(app.exec_())

