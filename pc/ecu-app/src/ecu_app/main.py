from PySide6.QtGui import QIcon, QKeySequence
from PySide6.QtWidgets import QMainWindow, QApplication


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("STM32 ECU Tool")

        # Menu
        self.menu = self.menuBar()
        file_menu = self.menu.addMenu("File")

        # Exit QAction
        file_menu.addAction(QIcon.fromTheme(QIcon.ThemeIcon.ApplicationExit),
        "Exit", QKeySequence.StandardKey.Quit, self.close)
            
        # Status Bar
        self.status = self.statusBar()
        self.status.showMessage("ECU connected: NO")

        # Window dimensions
        #geometry = self.screen().availableGeometry()
        self.setFixedSize(1200, 800)

if __name__ == "__main__":
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()

