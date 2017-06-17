#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp, QLineEdit, QLabel, QWidget, QPlainTextEdit, QPushButton, QVBoxLayout,QGridLayout, QSpinBox
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
	dspin = None
	xspin = None
	yspin = None
	deltaspin = None
	lrender = None
	mainwidget = None

	def toolbarsetup(self):
		''' Adds toolbar to the application. '''
		renderAction = QAction(QIcon.fromTheme("applications-science"), 'Render', self)
		renderAction.setShortcut('Ctrl+R')
		renderAction.triggered.connect(self.signalRender)

		settingsAction = QAction(QIcon.fromTheme("document-properties"), 'Settings', self)
		settingsAction.setShortcut('Ctrl+P')
		settingsAction.triggered.connect(self.signalRender)

		self.toolbar = self.addToolBar('Tools')
		self.toolbar.addAction(renderAction)
		self.toolbar.addAction(settingsAction)

	def layoutsetup(self):
		''' Adds widgets to the application. '''
		self.mainwidget = QWidget(self)
		self.setCentralWidget(self.mainwidget)

		vbox = QVBoxLayout()
		self.lrender = LWidget()

		# Axiom editor
		vargrid = QGridLayout()
		alabel = QLabel("Axiom")
		vargrid.addWidget(alabel,0,0)
		self.aedit = QLineEdit()
		vargrid.addWidget(self.aedit,0,1)

		# Variable editor
		vlabel = QLabel("Variables")
		vargrid.addWidget(vlabel,1,0)
		self.vedit = QPlainTextEdit()
		vargrid.addWidget(self.vedit,1,1)

		# Align with innergrid
		dgrid = QGridLayout()

		# Depth spinner
		dlabel = QLabel("Depth")
		dgrid.addWidget(dlabel,0,0)
		self.dspin = QSpinBox()
		self.dspin.setMinimum(0)
		self.dspin.setMaximum(99)
		self.dspin.setValue(1)
		dgrid.addWidget(self.dspin,0,1)

		# Inner grid to utilize space next to varedit
		innergrid = QGridLayout()

		# Scale spinner
		slabel = QLabel("Scale")
		innergrid.addWidget(slabel,0,0)
		self.sspin = QSpinBox()
		self.sspin.setMinimum(1)
		self.sspin.setMaximum(99)
		self.sspin.setValue(5)
		innergrid.addWidget(self.sspin,0,1)

		# Position spinner
		xlabel = QLabel("X:")
		self.xspin = QSpinBox()
		self.xspin.setRange(-1000,1000)
		innergrid.addWidget(xlabel, 1,0)
		innergrid.addWidget(self.xspin, 1,1)
		ylabel = QLabel("Y:")
		self.yspin = QSpinBox()
		self.yspin.setRange(-1000,1000)
		innergrid.addWidget(ylabel, 2,0)
		innergrid.addWidget(self.yspin, 2,1)

		# Angle spinner
		deltalabel = QLabel("delta:")
		innergrid.addWidget(deltalabel, 3,0)
		self.deltaspin = QSpinBox()
		self.deltaspin.setRange(0,360)
		self.deltaspin.setValue(90)
		innergrid.addWidget(self.deltaspin, 3,1)


		# Actual layout
		vbox.addWidget(self.lrender,1)
		vargrid.addLayout(dgrid, 0,2)
		vargrid.addLayout(innergrid, 1,2)
		vbox.addLayout(vargrid)
		self.mainwidget.setLayout(vbox)

	def windowsetup(self):
		''' General window setup. '''
		self.toolbarsetup()
		self.layoutsetup()

		self.setWindowTitle("L-Parser")
		self.show()

	def signalRender(self):
		''' Sets values for rendering in the rendering widget. '''
		self.lrender.valueSetEvent({"axiom":self.aedit.text(),
						"depth":self.dspin.value(),
						"env":self.vedit.toPlainText(),
						"scale":self.sspin.value(),
						"delta":self.deltaspin.value(),
						"xpos":self.xspin.value(),
						"ypos":self.yspin.value()})
	

if __name__ == "__main__":
	app = QApplication(sys.argv)
	render = LParseQT()
	sys.exit(app.exec_())

