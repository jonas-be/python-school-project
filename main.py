import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton

import size_converter
import number_converter


class StartGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Start GUI")

        # Create the central widget and layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        # Create buttons for each converter
        unit_converter_button = QPushButton("Unit Converter")
        unit_converter_button.clicked.connect(self.start_unit_converter)
        self.layout.addWidget(unit_converter_button)

        number_converter_button = QPushButton("Number Converter")
        number_converter_button.clicked.connect(self.start_number_converter)
        self.layout.addWidget(number_converter_button)

        subnet_calculator_button = QPushButton("Subnet Calculator")
        subnet_calculator_button.clicked.connect(self.start_subnet_calculator)
        self.layout.addWidget(subnet_calculator_button)

        # Initialize converter objects
        self.unit_converter = None
        self.number_converter = None

    def start_unit_converter(self):
        if not self.unit_converter:
            self.unit_converter = size_converter.UnitConverter()
        self.unit_converter.show()

    def start_number_converter(self):
        if not self.number_converter:
            self.number_converter = number_converter.NumberConverter()
        self.number_converter.show()

    def start_subnet_calculator(self):
        print("Need to be implemented")
        # subnet_calculator = SubnetCalculator()
        # subnet_calculator.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    start_gui = StartGUI()
    start_gui.show()
    sys.exit(app.exec())
