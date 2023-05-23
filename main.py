import sys

from PyQt6.QtWidgets import QApplication

import size_converter

if __name__ == "__main__":
    app = QApplication(sys.argv)
    converter = size_converter.UnitConverter()
    converter.show()
    sys.exit(app.exec())
