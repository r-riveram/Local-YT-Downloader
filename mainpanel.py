from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog
import sys
import mp3downloader
import mp4downloader
from designer import Ui_MainWindow 


class MainWindow(QMainWindow, Ui_MainWindow): 
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.destination_folder = None

        self.buttonmp4.clicked.connect(self.descargar_mp4)
        self.buttonmp3.clicked.connect(self.descargar_mp3)
        self.pushButton.clicked.connect(self.select_folder)

    def select_folder(self):
        folder = QFileDialog.getExistingDirectory(self, 'Seleccionar carpeta')
        if folder:
            self.destination_folder = folder
            self.statusbar.showMessage(f'Carpeta seleccionada: {folder}')

    def descargar_mp4(self):
        enlace = self.url.toPlainText()

        if not self.destination_folder:
            self.statusbar.showMessage('Por favor, seleccione una carpeta de destino.')
            return

        mensaje = mp4downloader.descargar_mp4(enlace, self.destination_folder)
        self.statusbar.showMessage(mensaje)

    def descargar_mp3(self):
        enlace = self.url.toPlainText()

        if not self.destination_folder:
            self.statusbar.showMessage('Por favor, seleccione una carpeta de destino.')
            return

        mensaje = mp3downloader.descargar_mp3(enlace, self.destination_folder)
        self.statusbar.showMessage(mensaje)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
