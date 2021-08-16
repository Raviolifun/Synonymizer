from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5 import QtGui
from functools import partial
from src.main.python import Sub_Functions
from pathlib import Path

import sys

__version__ = '1.0'
__author__ = 'Oren Anderson'


# Create a subclass of QMainWindow to setup the calculator's GUI
class ThesaurusPlusUi(QMainWindow):
    """PyCalc's View (GUI)."""
    def __init__(self):
        """View initializer."""
        super().__init__()

        # Set some main window's properties
        self.setWindowTitle('Thesaurus Plus')
        self.setWindowIcon(QtGui.QIcon('..\\icons\\Phrog.ico'))
        self.setMinimumSize(700, 400)

        # Set Central Widget
        self._central_widget = QWidget(self)
        self.setCentralWidget(self._central_widget)

        # Set the general layout
        self._general_layout = QVBoxLayout()
        self._central_widget.setLayout(self._general_layout)

        # Create menu and the content/text fields
        self._create_menu()
        self._create_content()

    def _create_menu(self):
        self.top_menu_layout = QHBoxLayout()
        self._general_layout.addLayout(self.top_menu_layout)

        self.run = QPushButton('Run')
        self.top_menu_layout.addWidget(self.run)
        self.re_running = QPushButton('Re-Running')
        self.top_menu_layout.addWidget(self.re_running)
        self.import_text = QPushButton('Import')
        self.top_menu_layout.addWidget(self.import_text)

    def _create_content(self):
        self.primary_layout = QVBoxLayout()
        self._general_layout.addLayout(self.primary_layout)

        self.primary_layout.addWidget(QLabel('Input Text'))
        self.input_text = QPlainTextEdit('Type text here or use the import button to import larger files')
        self.primary_layout.addWidget(self.input_text)

        self.primary_layout.addWidget(QLabel('Output Text'))
        self.output_text = QPlainTextEdit()
        self.primary_layout.addWidget(self.output_text)

    def set_input_text(self, text):
        self.input_text.setPlainText(text)
        self.input_text.setFocus()

    def clear_input_text(self):
        self.set_input_text('')

    def get_input_text(self):
        return self.input_text.text()

    def set_output_text(self, text):
        self.output_text.setPlainText(text)
        self.output_text.setFocus()


# Create a Controller class to connect the UI
class PyCalcCtrl:
    def __init__(self, view):
        """Controller initializer."""
        self._view = view
        # Connect signals and slots
        self._connect_signals()

    def _import_text(self):
        # open file dialog box, navigation starting at home directory
        print("test2")
        home_dir = str(Path.home())
        file_name = QFileDialog.getOpenFileName(caption='Open Text File', directory=home_dir,
                                                filter="txt files (*.txt *.docx)")
        file_name = file_name[0]
        if file_name is not '':
            with open(file_name[0], "r") as fh:
                self._view.set_input_text(fh.read())

    def _run_input(self):
        print("test3")
        text_input = self._view.get_input_text()
        output = Sub_Functions.synoantonym_string(text_input, "a an the i it as its no in", True)
        self._view.set_output_text(output)

    def _connect_signals(self):
        print(self._view.import_text)
        self._view.run.clicked.connect(self._run_input)
        self._view.re_running.clicked.connect(self._import_text)
        self._view.import_text.clicked.connect(self._import_text)


# Client code
def main():
    """Main function."""
    # Create an instance of `QApplication`
    app = QApplication(sys.argv)

    # Download or update language toolkit
    Sub_Functions.download()

    # Load qss (qt equivalent of css)
    sshFile = "customLooks.qss"
    with open(sshFile, "r") as fh:
        app.setStyleSheet(fh.read())

    # Show the calculator's GUI
    view = ThesaurusPlusUi()
    view.show()

    # Create instances of the model and the controller
    PyCalcCtrl(view)

    # Execute calculator's main loop
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
