import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QHBoxLayout, QWidget, QLineEdit, QComboBox, QPushButton

class NumberConverter(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Number Converter")

        # Create the central widget and layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        # Create the input field
        value_label = QLabel("Enter the value:")
        self.layout.addWidget(value_label)
        self.value_entry = QLineEdit()
        self.layout.addWidget(self.value_entry)

        # Create a layout for the input unit
        from_unit_layout = QHBoxLayout()
        self.layout.addLayout(from_unit_layout)

        from_unit_label = QLabel("From:")
        from_unit_layout.addWidget(from_unit_label)

        # Create a dropdown menu for the input unit
        self.from_unit_menu = QComboBox()
        self.from_unit_menu.addItem("Decimal")
        self.from_unit_menu.addItem("Hexadecimal")
        self.from_unit_menu.addItem("Binary")
        from_unit_layout.addWidget(self.from_unit_menu)

        # Create a layout for the output unit
        to_unit_layout = QHBoxLayout()
        self.layout.addLayout(to_unit_layout)

        to_unit_label = QLabel("To:")
        to_unit_layout.addWidget(to_unit_label)

        # Create a dropdown menu for the output unit
        self.to_unit_menu = QComboBox()
        self.to_unit_menu.addItem("Decimal")
        self.to_unit_menu.addItem("Hexadecimal")
        self.to_unit_menu.addItem("Binary")
        to_unit_layout.addWidget(self.to_unit_menu)

        # Create a label for the output value
        result_label = QLabel("Result:")
        self.layout.addWidget(result_label)

        # Create a label to display the output value
        self.result_display = QLabel()
        self.layout.addWidget(self.result_display)

        # Create a button to initiate the conversion
        convert_button = QPushButton("Convert")
        convert_button.clicked.connect(self.convert_numbers_and_update_display)
        self.layout.addWidget(convert_button)

    def convert_numbers_and_update_display(self):
        try:
            value = self.value_entry.text()
            from_unit = self.from_unit_menu.currentText()
            to_unit = self.to_unit_menu.currentText()
            result = convert_numbers(value, from_unit, to_unit)
            self.result_display.setText(result)
        except ValueError:
            self.result_display.setText("Invalid input")

def convert_numbers(value, from_unit, to_unit):
    if from_unit == "Decimal" and to_unit == "Hexadecimal":
        return hex(int(value))[2:]
    elif from_unit == "Decimal" and to_unit == "Binary":
        return bin(int(value))[2:]
    elif from_unit == "Hexadecimal" and to_unit == "Decimal":
        return str(int(value, 16))
    elif from_unit == "Hexadecimal" and to_unit == "Binary":
        decimal_value = int(value, 16)
        return bin(decimal_value)[2:]
    elif from_unit == "Binary" and to_unit == "Decimal":
        return str(int(value, 2))
    elif from_unit == "Binary" and to_unit == "Hexadecimal":
        decimal_value = int(value, 2)
        return hex(decimal_value)[2:]
    else:
        return value

if __name__ == "__main__":
    app = QApplication(sys.argv)
    converter = NumberConverter()
    converter.show()
    sys.exit(app.exec())