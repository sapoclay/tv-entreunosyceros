import os
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtWebEngineWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setGeometry(100, 100, 1200, 760)
        MainWindow.setMinimumSize(400, 500)
        MainWindow.setWindowTitle("A3Series")  # Agrega un título personalizado
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.webEngineView = QtWebEngineWidgets.QWebEngineView(self.centralwidget)
        self.verticalLayout.addWidget(self.webEngineView)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
    
        self.webEngineView.setUrl(QtCore.QUrl("https://www.atresplayer.com/directos/atreseries/"))
        self.webEngineView.setObjectName("webEngineView")
        MainWindow.setCentralWidget(self.centralwidget)

        icon_path = os.path.join(os.path.dirname(sys.argv[0]), "iconos/a3series.ico")
        MainWindow.setWindowIcon(QtGui.QIcon(icon_path)) 

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myappid = 'entreunosyceros.tv.subproduct.01'
    if sys.platform == 'win32':
        import ctypes
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())