from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QLabel, QFileDialog
import sys
import mp3downloader
import mp4downloader

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('YouTube Downloader')
        self.setGeometry(100, 100, 500, 200)

        self.destination_folder = None
        layout_principal = QVBoxLayout()
        layout_video = QHBoxLayout()
        self.lbl_video = QLabel('Enlace del video:', self)
        layout_video.addWidget(self.lbl_video)
        self.txt_enlace = QLineEdit(self)
        layout_video.addWidget(self.txt_enlace)
        layout_principal.addLayout(layout_video)

        layout_botones = QHBoxLayout()
        btn_descargar_mp4 = QPushButton('Descargar MP4', self)
        btn_descargar_mp4.clicked.connect(self.descargar_mp4)
        layout_botones.addWidget(btn_descargar_mp4)

        btn_descargar_mp3 = QPushButton('Descargar MP3', self)
        btn_descargar_mp3.clicked.connect(self.descargar_mp3)
        layout_botones.addWidget(btn_descargar_mp3)
        layout_principal.addLayout(layout_botones)

        btn_select_folder = QPushButton('Seleccionar ruta', self)
        btn_select_folder.clicked.connect(self.select_folder)
        layout_principal.addWidget(btn_select_folder)

        self.lbl_estado = QLabel(self)
        layout_principal.addWidget(self.lbl_estado)

        self.lbl_folder = QLabel(self)
        layout_principal.addWidget(self.lbl_folder)

        self.setLayout(layout_principal)
        self.show()

    def select_folder(self):
        folder = QFileDialog.getExistingDirectory(self, 'Seleccionar carpeta')
        if folder:
            self.destination_folder = folder
            self.lbl_folder.setText(f'Carpeta seleccionada: {folder}')

    def descargar_mp4(self):
        enlace = self.txt_enlace.text()

        if not self.destination_folder:
            self.lbl_estado.setText('Por favor, seleccione una carpeta de destino.')
            return

        mensaje = mp4downloader.descargar_mp4(enlace, self.destination_folder)
        self.lbl_estado.setText(mensaje)

    def descargar_mp3(self):
        enlace = self.txt_enlace.text()

        if not self.destination_folder:
            self.lbl_estado.setText('Por favor, seleccione una carpeta de destino.')
            return

        mensaje = mp3downloader.descargar_mp3(enlace, self.destination_folder)
        self.lbl_estado.setText(mensaje)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
