from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5 import QtGui
from functools import partial

import sys

__version__ = '0.1'
__author__ = 'Oren Anderson'

# Create a subclass of QMainWindow to setup the calculator's GUI
class PyCalcUi(QMainWindow):
    """PyCalc's View (GUI)."""
    def __init__(self):
        """View initializer."""
        super().__init__()

        # Set some main window's properties
        self.setWindowTitle('Thesaurus Plus')
        self.setWindowIcon(QtGui.QIcon('..\\icons\\Phrog.ico'))
        self.setMinimumSize(700, 400)

        # Set the central widget and the general layout
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

        # Set Central Widget
        self._central_widget = QWidget(self)
        self.setCentralWidget(self._central_widget)

        # Set the general layout
        self._general_layout = QVBoxLayout()
        self._central_widget.setLayout(self._general_layout)

        # Create the display and the buttons
        self._create_menu()
        self._create_content()

    def _create_menu(self):
        self.top_menu_layout = QHBoxLayout()
        self.top_menu_layout.addWidget(QPushButton('Run'))
        self.top_menu_layout.addWidget(QPushButton('Recycle'))
        self.top_menu_layout.addWidget(QPushButton('Import'))
        self._general_layout.addLayout(self.top_menu_layout)

    def _create_content(self):
        self.primary_layout = QVBoxLayout()
        self.primary_layout.addWidget(QLabel('Input Text'))
        self.primary_layout.addWidget(QPlainTextEdit())
        self.primary_layout.addWidget(QLabel('Output Text'))
        self.primary_layout.addWidget(QPlainTextEdit())
        self._general_layout.addLayout(self.primary_layout)

    # def setDisplayText(self, text):
    #     """Set display's text."""
    #     self.display.setText(text)
    #     self.display.setFocus()
    #
    # def displayText(self):
    #     """Get display's text."""
    #     return self.display.text()
    #
    # def clearDisplay(self):
    #     """Clear the display."""
    #     self.setDisplayText('')


# Create a Controller class to connect the GUI and the model
# class PyCalcCtrl:
#     """PyCalc's Controller."""
#     def __init__(self, model, view):
#         """Controller initializer."""
#         self._evaluate = model
#         self._view = view
#         # Connect signals and slots
#         self._connectSignals()
#
#     def _calculateResult(self):
#         """Evaluate expressions."""
#         result = self._evaluate(expression=self._view.displayText())
#         self._view.setDisplayText(result)
#
#     def _buildExpression(self, sub_exp):
#         """Build expression."""
#         if self._view.displayText() == ERROR_MSG:
#             self._view.clearDisplay()
#
#         expression = self._view.displayText() + sub_exp
#         self._view.setDisplayText(expression)
#
#     def _connectSignals(self):
#         """Connect signals and slots."""
#         for btnText, btn in self._view.buttons.items():
#             if btnText not in {'=', 'C'}:
#                 btn.clicked.connect(partial(self._buildExpression, btnText))
#
#         self._view.buttons['='].clicked.connect(self._calculateResult)
#         self._view.display.returnPressed.connect(self._calculateResult)
#         self._view.buttons['C'].clicked.connect(self._view.clearDisplay)


# Client code
def main():
    """Main function."""
    # Create an instance of `QApplication`
    app = QApplication(sys.argv)

    # Load qss (qt equivalent of css)
    sshFile = "customLooks.qss"
    with open(sshFile, "r") as fh:
        app.setStyleSheet(fh.read())

    # Show the calculator's GUI
    view = PyCalcUi()
    view.show()
    # Create instances of the model and the controller
    # model = evaluateExpression
    # PyCalcCtrl(model=model, view=view)
    # Execute calculator's main loop
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
