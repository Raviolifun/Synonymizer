from PyQt5.QtGui import QIntValidator
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
    def __init__(self):
        super().__init__()

        # Set some main window's properties
        self.setWindowTitle('Thesaurus Plus')
        self.setWindowIcon(QtGui.QIcon('..\\icons\\Phrog.ico'))
        self.setMinimumSize(700, 400)

        # Initialize re-running dialog box popup
        self.dialog_box = PopUpBox()

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
        return self.input_text.toPlainText()

    def set_output_text(self, text):
        self.output_text.setPlainText(text)
        self.output_text.setFocus()

    def get_output_text(self):
        return self.output_text.toPlainText()


class PopUpBox(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Re-Running options')
        dlg_layout = QVBoxLayout()
        form_layout = QFormLayout()

        # re-run inputs
        self.onlyInt = QIntValidator(1, 100, self)
        self.number_of_runs = QLineEdit('20')
        self.number_of_runs.setValidator(self.onlyInt)

        self.detailed_output = QCheckBox()

        form_layout.addRow('Number of runs:', self.number_of_runs)
        form_layout.addRow('Detailed Output:', self.detailed_output)
        dlg_layout.addLayout(form_layout)

        btns = QDialogButtonBox()
        btns.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)
        dlg_layout.addWidget(btns)

        self.setLayout(dlg_layout)

    def display_dialog(self):
        self.show()


# Create a Controller class to connect the UI
class PyCalcCtrl:
    def __init__(self, view):
        """Controller initializer."""
        self._view = view
        # Connect signals and slots
        self._connect_signals()

    def _import_text(self):
        # open file dialog box, navigation starting at home directory
        home_dir = str(Path.home())
        file_name = QFileDialog.getOpenFileName(caption='Open Text File', directory=home_dir,
                                                filter="txt files (*.txt *.docx)")
        file_name = file_name[0]
        if file_name is not '':
            with open(file_name, "r") as fh:
                import_text = fh.read()
                self._view.set_input_text(import_text)

    def _run_input(self):
        text_input = self._view.get_input_text()
        output = Sub_Functions.synoantonym_string(text_input, "a an the i it as its no in", True)
        self._view.set_output_text(output)

    def _re_run_input(self):

        # pop up dialog box with 20 as default value (something must be input, thing must be integer number)
        # run button to run with whatever is in the box
        # cancel button to exit out of dialog box (does not run)

        self._view.setEnabled(False)
        self._view.dialog_box.display_dialog()
        number_of_runs = int(self._view.dialog_box.number_of_runs.text())
        show_intermediate = bool(self._view.dialog_box.detailed_output.checkState())

        total = ""
        output = self._view.get_input_text()
        for i in range(number_of_runs):
            output = Sub_Functions.synoantonym_string(output, "a an the i it as its no in", True)
            if show_intermediate:
                if i == number_of_runs - 1:
                    total = total + str(i + 1) + ": " + output
                else:
                    total = total + str(i + 1) + ": " + output + "\n"
        if show_intermediate:
            self._view.set_output_text(total)
        else:
            self._view.set_output_text(output)



    # def _edit_ignored_words

    def _connect_signals(self):
        self._view.run.clicked.connect(partial(self._run_input))
        # self._view.re_running.clicked.connect(partial(self._re_run_input))
        self._view.re_running.clicked.connect(partial(self._re_run_input))
        self._view.import_text.clicked.connect(partial(self._import_text))


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
