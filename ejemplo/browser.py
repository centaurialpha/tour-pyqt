from PyQt5.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QLabel,
    QLineEdit,
    QApplication,
    QStatusBar,
    QProgressBar
)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QUrl
from PyQt5.QtWebKitWidgets import QWebView


class Browser(QWidget):

    def __init__(self):
        super(Browser, self).__init__()
        self.setWindowTitle("Navegador PyConAr 2016")
        vbox = QVBoxLayout(self)  # Contenedor principal
        hbox = QHBoxLayout()  # Contenedor horizontal
        # Widgets
        btn_atras = QPushButton(QIcon.fromTheme("back"), '')
        btn_adelante = QPushButton(QIcon.fromTheme("forward"), '')
        btn_ok = QPushButton(QIcon.fromTheme("find"), '')
        btn_parar = QPushButton(QIcon.fromTheme("cancel"), '')
        btn_reload = QPushButton(QIcon.fromTheme("reload"), '')
        self.url = QLineEdit()
        self.url.setPlaceholderText("Ingresa una página web o busca en Google")
        # Agrego los widgets
        hbox.addWidget(btn_atras)
        hbox.addWidget(btn_adelante)
        hbox.addWidget(btn_parar)
        hbox.addWidget(btn_reload)
        hbox.addWidget(self.url)
        hbox.addWidget(btn_ok)
        # Agrego el contenedor horizontal al vertical
        vbox.addLayout(hbox)
        # Componente web
        self.web = QWebView()
        vbox.addWidget(self.web)
        # Creo una barra de estado
        self.estado = QStatusBar()
        self.estado.hide()
        # Creo una barra de progreso y la agrego a la barra de estado
        self.prog = QProgressBar()
        self.estado.addWidget(self.prog, 1)
        self.estado.addWidget(QLabel("Cargando..."))
        vbox.addWidget(self.estado)

        # Conexiones
        btn_atras.clicked.connect(self.web.back)
        btn_adelante.clicked.connect(self.web.forward)
        btn_parar.clicked.connect(self.web.stop)
        btn_reload.clicked.connect(self.web.reload)
        btn_ok.clicked.connect(self._cargar_pagina)
        self.web.loadProgress.connect(self.prog.setValue)
        self.web.loadFinished.connect(self._carga_terminada)
        self.url.returnPressed.connect(self._cargar_pagina)

    def _carga_terminada(self):
        self.estado.hide()
        self.url.setText(self.web.url().toString())

    def _cargar_pagina(self):
        if not self.estado.isVisible():
            self.estado.show()
        text = self.url.text()
        if text.find('.') != -1 and not text.startswith('http://'):
            url = 'http://' + text
        else:
            url = 'http://google.com/search?q=' + text.replace(' ', '+')
        self.web.load(QUrl(url))

if __name__ == "__main__":
    import sys

    app = QApplication([])
    w = Browser()
    w.show()
    sys.exit(app.exec_())
