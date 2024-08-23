from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("YouTube Downloader")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("""
            QMainWindow {
                background-color: #2b2b2b;
                color: #ffffff;
            }
            QLabel {
                color: #ffffff;
                font-size: 14px;
            }
            QLineEdit, QComboBox {
                background-color: #3b3b3b;
                color: #ffffff;
                border: 1px solid #555555;
                padding: 5px;
                border-radius: 3px;
                font-size: 14px;
            }
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border: none;
                padding: 8px 16px;
                border-radius: 4px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
            QPushButton:pressed {
                background-color: #3e8e41;
            }
            QProgressBar {
                border: 2px solid #555555;
                border-radius: 5px;
                text-align: center;
                color: #ffffff;
            }
            QProgressBar::chunk {
                background-color: #4CAF50;
                width: 10px;
                margin: 0.5px;
            }
        """)

        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        layout = QtWidgets.QVBoxLayout(self.centralwidget)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(15)

        # URL input
        url_layout = QtWidgets.QHBoxLayout()
        self.url_label = QtWidgets.QLabel("YouTube URL:", parent=self.centralwidget)
        url_layout.addWidget(self.url_label)

        self.url_input = QtWidgets.QLineEdit(parent=self.centralwidget)
        url_layout.addWidget(self.url_input)

        layout.addLayout(url_layout)

        # Folder selection
        folder_layout = QtWidgets.QHBoxLayout()
        self.folder_label = QtWidgets.QLabel("Save to:", parent=self.centralwidget)
        folder_layout.addWidget(self.folder_label)

        self.folder_input = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.folder_input.setReadOnly(True)
        folder_layout.addWidget(self.folder_input)

        self.folder_button = QtWidgets.QPushButton("Browse", parent=self.centralwidget)
        folder_layout.addWidget(self.folder_button)

        layout.addLayout(folder_layout)

        # Format and quality selection
        options_layout = QtWidgets.QHBoxLayout()

        self.format_combo = QtWidgets.QComboBox(parent=self.centralwidget)
        self.format_combo.addItems(["MP4", "MP3"])
        options_layout.addWidget(self.format_combo)

        self.quality_combo = QtWidgets.QComboBox(parent=self.centralwidget)
        self.quality_combo.addItems(["Highest", "720p", "480p", "360p"])
        options_layout.addWidget(self.quality_combo)

        self.download_button = QtWidgets.QPushButton("Download", parent=self.centralwidget)
        options_layout.addWidget(self.download_button)

        layout.addLayout(options_layout)

        # Progress bar
        self.progress_bar = QtWidgets.QProgressBar(parent=self.centralwidget)
        layout.addWidget(self.progress_bar)

        # Status label
        self.status_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.status_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.status_label)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "YouTube Downloader"))
        self.download_button.setText(_translate("MainWindow", "Download"))
        self.folder_button.setText(_translate("MainWindow", "Browse"))
