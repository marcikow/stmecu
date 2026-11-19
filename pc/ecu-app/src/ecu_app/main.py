from PySide6.QtGui import QIcon, QKeySequence
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ecu_connected = False

        self.setWindowTitle("STM32 ECU Tool")

        # Menu
        self.menu = self.menuBar()
        file_menu = self.menu.addMenu("File")

        # Exit QAction
        file_menu.addAction(QIcon.fromTheme(QIcon.ThemeIcon.ApplicationExit),
        "Exit", QKeySequence.StandardKey.Quit, self.close)

        # Window dimensions
        #geometry = self.screen().availableGeometry()
        self.setFixedSize(1200, 800)

        # Layout
        main_layout = QVBoxLayout()

        main_layout.setContentsMargins(15, 15, 15, 15)

        # Central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Set layout
        central_widget.setLayout(main_layout)

        # Label
        label = QLabel("STM32 ECU TOOL")
        main_layout.addWidget(label)

        # HLayout
        h_layout = QHBoxLayout()

        # Left panel
        left_panel = QWidget()
        left_layout = QVBoxLayout()
        left_panel.setLayout(left_layout)
        h_layout.addWidget(left_panel, 1)

        # Right panel
        right_panel = QWidget()
        right_layout = QVBoxLayout()
        right_panel.setLayout(right_layout)
        h_layout.addWidget(right_panel, 3)

        main_layout.addLayout(h_layout)

        # ECU STATUS LABELS
        status_label = QLabel("ECU STATUS")
        #status_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        left_layout.addWidget(status_label)

        self.conn_label = QLabel("Connected: NO")
        self.conn_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        left_layout.addWidget(self.conn_label)

        transp_label = QLabel("Transport: ---")
        transp_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        left_layout.addWidget(transp_label)

        ecu_volt_label = QLabel("ECU Voltage: ---")
        ecu_volt_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        left_layout.addWidget(ecu_volt_label)

        # LEFT PANEL BUTTONS
        connect_button = QPushButton("Connect ECU")
        connect_button.clicked.connect(self.connect_ecu)
        left_layout.addWidget(connect_button)

        disconnect_button = QPushButton("Disconnect ECU")
        disconnect_button.clicked.connect(self.disconnect_ecu)
        left_layout.addWidget(disconnect_button)

        # LIVE DATA LABELS
        live_data_label = QLabel("LIVE DATA")
        #live_data_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        right_layout.addWidget(live_data_label)

        rpm_label = QLabel("RPM: ---")
        rpm_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        right_layout.addWidget(rpm_label)

        map_label = QLabel("MAP: ---")
        map_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        right_layout.addWidget(map_label)

        tps_label = QLabel("TPS: ---")
        tps_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        right_layout.addWidget(tps_label)

        coolant_temp_label = QLabel("Coolant Temp: ---")
        coolant_temp_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        right_layout.addWidget(coolant_temp_label)

        iat_label = QLabel("IAT: ---")
        iat_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        right_layout.addWidget(iat_label)

        # Status Bar
        self.status = self.statusBar()
        self.status.showMessage("ECU " + self.conn_label.text())

    def connect_ecu(self):
        self.ecu_connected = True
        self.conn_label.setText("Connected: YES")
        self.status.showMessage("ECU " + self.conn_label.text())

    def disconnect_ecu(self):
        self.ecu_connected = False
        self.conn_label.setText("Connected: NO")
        self.status.showMessage("ECU " + self.conn_label.text())

    
if __name__ == "__main__":
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()

