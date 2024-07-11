from PyQt6.QtWidgets import QMainWindow, QTextEdit, QLineEdit, QPushButton, QApplication
import sys
from backend import Chatbot

class ChatbotWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setMinimumSize(700, 500)

        # Add chat area widget
        # giving self as arg applies the widget to self, ie the main window
        self.chat_area = QTextEdit(self)
        self.chat_area.setGeometry(10, 10, 480, 320)  # args: 2 coordinates, 2 dimensions
        self.chat_area.setReadOnly(True)

        # Add input field widget
        self.input_field = QLineEdit(self)
        self.input_field.setGeometry(10, 340, 480, 40)

        # Add button
        self.button = QPushButton("send", self)
        self.button.setGeometry(500, 340, 100, 40)
        self.button.clicked.connect(self.call_bot)

        self.show()

    def call_bot(self):
        user_input = self.input_field



app = QApplication(sys.argv)
main_window = ChatbotWindow()
main_window.show()
sys.exit(app.exec())