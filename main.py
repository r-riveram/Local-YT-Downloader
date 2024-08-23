from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt6.QtCore import QThread, pyqtSignal
import sys
import os

from designer import Ui_MainWindow
from mp4downloader import descargar_mp4
from mp3downloader import descargar_mp3


class DownloadThread(QThread):
    progress_signal = pyqtSignal(int)
    finished_signal = pyqtSignal(str)

    def __init__(self, url, output_path, format, quality):
        super().__init__()
        self.url = url
        self.output_path = output_path
        self.format = format
        self.quality = quality

    def run(self):
        try:
            if self.format == "MP4":
                message = descargar_mp4(self.url, self.output_path, self.quality, self.progress_callback)
            else:
                message = descargar_mp3(self.url, self.output_path, self.progress_callback)
            self.finished_signal.emit(message)
        except Exception as e:
            self.finished_signal.emit(f"Error: {str(e)}")

    def progress_callback(self, stream, chunk, bytes_remaining):
        total_size = stream.filesize
        bytes_downloaded = total_size - bytes_remaining
        percentage = int(bytes_downloaded / total_size * 100)
        self.progress_signal.emit(percentage)

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.folder_button.clicked.connect(self.select_folder)
        self.download_button.clicked.connect(self.start_download)
        self.format_combo.currentTextChanged.connect(self.toggle_quality_combo)

    def select_folder(self):
        folder = QFileDialog.getExistingDirectory(self, 'Select folder')
        if folder:
            self.folder_input.setText(folder)

    def toggle_quality_combo(self, format):
        self.quality_combo.setEnabled(format == "MP4")

    def start_download(self):
        url = self.url_input.text()
        output_path = self.folder_input.text()
        format = self.format_combo.currentText()
        quality = self.quality_combo.currentText() if format == "MP4" else None

        if not url or not output_path:
            self.status_label.setText("Please enter a URL and select a folder.")
            return

        self.download_thread = DownloadThread(url, output_path, format, quality)
        self.download_thread.progress_signal.connect(self.update_progress)
        self.download_thread.finished_signal.connect(self.download_finished)
        self.download_thread.start()

        self.download_button.setEnabled(False)
        self.status_label.setText("Downloading...")

    def update_progress(self, percentage):
        self.progress_bar.setValue(percentage)

    def download_finished(self, message):
        self.status_label.setText(message)
        self.download_button.setEnabled(True)
        self.progress_bar.setValue(0)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
