import os  # Importa el módulo "os" para manejar archivos y rutas del sistema operativo
import sys  # Importa el módulo "sys" para acceder a variables y funciones específicas del intérprete de Python
from PyQt5 import QtCore, QtGui, QtWidgets  # Importa los módulos necesarios de PyQt5
from PyQt5 import QtWebEngineWidgets  # Importa el módulo "QtWebEngineWidgets" de PyQt5

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setGeometry(100, 100, 1200, 760)  # Establece la geometría de la ventana principal
        MainWindow.setMinimumSize(400, 500)  # Establece el tamaño mínimo de la ventana principal
        MainWindow.setWindowTitle("Servicio MiTele")  # Establece el título de la ventana principal
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)  # Crea un layout vertical para el widget central
        self.webEngineView = QtWebEngineWidgets.QWebEngineView(self.centralwidget)  # Crea un widget de vista web
        self.verticalLayout.addWidget(self.webEngineView)  # Añade la vista web al layout vertical
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)  # Establece los márgenes del layout

        self.webEngineView.setUrl(QtCore.QUrl("https://www.mitele.es/"))  # Establece la URL de la vista web
        self.webEngineView.setObjectName("webEngineView")  # Establece el nombre del objeto de la vista web
        MainWindow.setCentralWidget(self.centralwidget)  # Establece el widget central de la ventana principal

        icon_path = os.path.join(os.path.dirname(sys.argv[0]), "iconos/mitele.ico")  # Obtiene la ruta del icono
        MainWindow.setWindowIcon(QtGui.QIcon(icon_path))  # Establece el icono de la ventana principal

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)  # Crea una instancia de la aplicación Qt
    myappid = 'entreunosyceros.tv.subproduct.01'  # Identificador de la aplicación
    if sys.platform == 'win32':  # Si el sistema operativo es Windows
        import ctypes
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)  # Establece el identificador de la aplicación
    MainWindow = QtWidgets.QMainWindow()  # Crea una instancia de la ventana principal
    ui = Ui_MainWindow()  # Crea una instancia de la clase de interfaz de usuario
    ui.setupUi(MainWindow)  # Configura la interfaz de usuario
    MainWindow.show()  # Muestra la ventana principal
    sys.exit(app.exec_())  # Ejecuta la aplicación y espera a que se cierre