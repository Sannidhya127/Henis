import sys
import io
from PyQt5 import QtWidgets, QtGui, QtCore
import sys
import os
from kernel import Parser


class CustomInterpreter:
    def __init__(self):
        self.output_buffer = io.StringIO()

    def run_code(self, code):
        # Redirect stdout to capture print statements
        sys.stdout = self.output_buffer
        try:
            parser_instance = Parser()
            cti = code
            res = parser_instance.interpret(cti)
            print(res)
        except Exception as e:
            print(f"Error: {e}")
        finally:
            sys.stdout = sys.__stdout__

    def get_output(self):
        return self.output_buffer.getvalue()

class IDE(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Run Your Henis")
        self.setGeometry(100, 100, 800, 600)
        self.setStyleSheet("background-color: #2e2e2e; color: white;")

        self.interpreter = CustomInterpreter()

        # Central widget
        self.central_widget = QtWidgets.QWidget(self)
        self.setCentralWidget(self.central_widget)
        self.layout = QtWidgets.QVBoxLayout(self.central_widget)

        # Navigation Bar
        self.navbar = QtWidgets.QToolBar("Navigation")
        self.addToolBar(self.navbar)

        self.home_action = QtWidgets.QAction("Home", self)
        self.home_action.triggered.connect(self.show_home)
        self.navbar.addAction(self.home_action)

        self.about_action = QtWidgets.QAction("About", self)
        self.about_action.triggered.connect(self.show_about)
        self.navbar.addAction(self.about_action)

        self.theme_action = QtWidgets.QAction("Switch Theme", self)
        self.theme_action.triggered.connect(self.switch_theme)
        self.navbar.addAction(self.theme_action)

        # Code input area
        self.code_area = QtWidgets.QTextEdit(self)
        self.code_area.setStyleSheet("background-color: #1e1e1e; color: #c5c5c5; font-family: 'Courier New'; font-size: 14px;")
        self.code_area.setPlaceholderText("Write your code here...")
        self.layout.addWidget(self.code_area)

        # Run button
        self.run_button = QtWidgets.QPushButton("Run", self)
        self.run_button.setStyleSheet("background-color: #007acc; color: white; font-size: 12px;")
        self.run_button.clicked.connect(self.run_code)
        self.layout.addWidget(self.run_button)

        # Output area
        self.output_area = QtWidgets.QTextEdit(self)
        self.output_area.setReadOnly(True)
        self.output_area.setStyleSheet("background-color: #1e1e1e; color: #c5c5c5; font-family: 'Courier New'; font-size: 14px;")
        self.layout.addWidget(self.output_area)

    def run_code(self):
        self.output_area.clear()
        code = self.code_area.toPlainText()
        self.interpreter.run_code(code)
        output = self.interpreter.get_output()
        self.output_area.setPlainText(output)

    def switch_theme(self):
        # Toggle theme (basic example)
        if self.styleSheet() == "":
            self.setStyleSheet("background-color: #ffffff; color: black;")
            self.code_area.setStyleSheet("background-color: #f0f0f0; color: black; font-family: 'Courier New'; font-size: 14px;")
            self.output_area.setStyleSheet("background-color: #f0f0f0; color: black; font-family: 'Courier New'; font-size: 14px;")
        else:
            self.setStyleSheet("")
            self.code_area.setStyleSheet("background-color: #1e1e1e; color: #c5c5c5; font-family: 'Courier New'; font-size: 14px;")
            self.output_area.setStyleSheet("background-color: #1e1e1e; color: #c5c5c5; font-family: 'Courier New'; font-size: 14px;")

    def show_home(self):
        self.output_area.clear()
        self.output_area.setPlainText("Welcome to JavaNot IDE!\n\n"
                                       "Write your code above and hit 'Run'.")

    def show_about(self):
        self.output_area.clear()
        self.output_area.setPlainText("JavaNot IDE\n\n"
                                       "This is a simple interpreter for your custom esoteric programming language "
                                       "that humorously disses Java!\n"
                                       "Developed using Python and PyQt5.")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ide = IDE()
    ide.show()
    sys.exit(app.exec_())
