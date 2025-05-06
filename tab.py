import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIntValidator
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Input Dialog Program")
        self.setGeometry(100, 100, 300, 300)

        # Main widget and layout
        self.main_widget = QWidget()
        self.setCentralWidget(self.main_widget)
        self.main_layout = QVBoxLayout()  
        self.main_widget.setLayout(self.main_layout)

        # Add name and NIM label at the top
        self.name_creator = QLabel("Lalu Bisma Kurniawan Haris | F1D022055")
        self.name_creator.setAlignment(Qt.AlignCenter)
        self.main_layout.addWidget(self.name_creator)

        # Horizontal layout for buttons and displays
        self.content_layout = QHBoxLayout()

        # Left side: Buttons
        self.button_layout = QVBoxLayout()
        self.programming_button = QPushButton("Choose Programming Language")
        self.name_button = QPushButton("Get Name")
        self.number_button = QPushButton("Enter Integer")

        self.programming_button.clicked.connect(self.show_programming_dialog)
        self.name_button.clicked.connect(self.show_name_dialog)
        self.number_button.clicked.connect(self.show_number_dialog)

        self.button_layout.addWidget(self.programming_button)
        self.button_layout.addWidget(self.name_button)
        self.button_layout.addWidget(self.number_button)
        self.button_layout.addStretch()

        # Right side: Input display
        self.display_layout = QVBoxLayout()
        self.programming_display = QLineEdit()
        self.name_display = QLineEdit()
        self.number_display = QLineEdit()

        self.programming_display.setReadOnly(True)
        self.name_display.setReadOnly(True)
        self.number_display.setReadOnly(True)

        # self.display_layout.addWidget(QLabel("Selected Programming Language:"))
        self.display_layout.addWidget(self.programming_display)
        # self.display_layout.addWidget(QLabel("Entered Name:"))
        self.display_layout.addWidget(self.name_display)
        # self.display_layout.addWidget(QLabel("Entered Integer:"))
        self.display_layout.addWidget(self.number_display)
        self.display_layout.addStretch()

        # Add button and display layouts to content layout
        self.content_layout.addLayout(self.button_layout)
        self.content_layout.addLayout(self.display_layout)

        # Add content layout to main layout
        self.main_layout.addLayout(self.content_layout)

    def show_programming_dialog(self):
        items = ["Python", "Java", "C++", "JavaScript", "Ruby"]
        combo = QComboBox()
        combo.addItems(items)
        
        dialog = QInputDialog(self)
        dialog.setWindowTitle("Choose Programming Language")
        dialog.setLabelText("Select a programming language:")
        dialog.setComboBoxItems(items)
        dialog.setInputMode(QInputDialog.TextInput)
        dialog.setComboBoxEditable(False)
        
        # Connect custom combo box
        dialog.findChild(QComboBox).currentTextChanged.connect(lambda text: dialog.setTextValue(text))
        
        if dialog.exec_() == QInputDialog.Accepted:
            self.programming_display.setText(dialog.textValue())

    def show_name_dialog(self):
        text, ok = QInputDialog.getText(self, "Get Name", "Enter your name:")
        if ok and text:
            self.name_display.setText(text)

    def show_number_dialog(self):
        dialog = QInputDialog(self)
        dialog.setWindowTitle("Enter Integer")
        dialog.setLabelText("Select an integer:")
        dialog.setInputMode(QInputDialog.IntInput)
        
        # Configure spinbox
        spinbox = dialog.findChild(QSpinBox)
        spinbox.setRange(-1000000, 1000000)  
        spinbox.setValue(0)  
        
        if dialog.exec_() == QInputDialog.Accepted:
            self.number_display.setText(str(dialog.intValue()))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())