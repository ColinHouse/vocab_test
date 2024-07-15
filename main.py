import sys
from PySide6.QtWidgets import QApplication
from ui import VocabApp

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = VocabApp()
    window.show()
    sys.exit(app.exec())
