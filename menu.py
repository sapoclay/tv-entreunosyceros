import os
import sys
import subprocess
from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidget, QListWidgetItem
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QIcon, QFont


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.instalar_pygame() # Instalar Pygame al iniciar la aplicación

    def initUI(self):
        self.setWindowTitle('Menú de canales')
        self.setGeometry(100, 100, 400, 300)

        # Establecer el icono de la ventana principal
        self.setWindowIcon(QIcon('./icono.png'))

        # Crear un QListWidget para mostrar el contenido del directorio "canales"
        self.listWidget = QListWidget(self)
        self.setCentralWidget(self.listWidget)

        # Obtener los archivos Python en el directorio "canales" ordenados alfabéticamente
        canales_dir = './canales/'
        archivos = os.listdir(canales_dir)
        py_files = [archivo for archivo in archivos if archivo.endswith('.py')]
        py_files.sort() # Ordenar los archivos alfabéticamente

        # Crear un QListWidgetItem para cada archivo Python
        for py_file in py_files:
            item = QListWidgetItem(py_file)
            item.setToolTip(os.path.abspath(os.path.join(canales_dir, py_file)))
            self.listWidget.addItem(item)

        # Conectar la señal itemDoubleClicked al slot ejecutar_script
        self.listWidget.itemDoubleClicked.connect(self.ejecutar_script)

        # Aplicar estilo personalizado al listado de canales
        self.listWidget.setStyleSheet("""
            QListWidget {
                background-color: #F0F0F0;
                border: 1px solid #CCC;
                border-radius: 5px;
                padding: 5px;
                font-size: 14px;
            }
            QListWidget::item {
                background-color: #FFF;
                border-radius: 5px;
                padding: 5px;      
            }
            QListWidget::item:hover {
                background-color: #E6E6E6;
                color: #000;
                font-weight: bold;
            }
            QListWidget::item:selected {
                background-color: #BFBFBF;
                color: #000;
                font-weight: bold;
            }
        """)

        self.show()

    def instalar_pygame(self):
        # Instalar Pygame con Python 3
        try:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-U', 'pygame'])
        except subprocess.CalledProcessError as e:
            print(f"Error al instalar pygame: {e}")

    def ejecutar_script(self, item):
        # Ejecutar el archivo Python seleccionado con Python 3
        ruta_absoluta = item.toolTip()
        subprocess.Popen([sys.executable, ruta_absoluta])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    sys.exit(app.exec_())