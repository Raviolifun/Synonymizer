"""Vertical layout example."""

import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QPlainTextEdit
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QFileDialog
from pathlib import Path
from PyQt5 import QtGui

app = QApplication(sys.argv)

sshFile = "customLooks.qss"
with open(sshFile, "r") as fh:
    app.setStyleSheet(fh.read())

window = QWidget()
window.setWindowTitle('Synomizer')

# Top Menu
top_menu = QWidget()
top_menu_layout = QHBoxLayout()
top_menu_layout.addWidget(QPushButton('Run'))
top_menu_layout.addWidget(QPushButton('Recycle'))
top_menu_layout.addWidget(QPushButton('Import'))
top_menu.setLayout(top_menu_layout)

# Main Layout
central_layout = QVBoxLayout()
central_layout.addWidget(top_menu)
central_layout.addWidget(QLabel('Input Text'))
central_layout.addWidget(QPlainTextEdit())
central_layout.addWidget(QLabel('Output Text'))
central_layout.addWidget(QPlainTextEdit())

# Create Main Window
window.setLayout(central_layout)
window.setWindowIcon(QtGui.QIcon('..\\icons\\Phrog.ico'))
window.setMinimumSize(700, 400)
window.show()

# open file dialog box, navigation starting at home directory
home_dir = str(Path.home())
fileName = QFileDialog.getOpenFileName(caption='Open Text File', directory=home_dir, filter="txt files (*.txt *.docx)")

# Turn off app when exit is pressed
sys.exit(app.exec_())

