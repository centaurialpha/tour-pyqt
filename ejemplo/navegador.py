from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon
from PyQt5.QtWebKitWidgets import *


class Navegador(QWidget):

    def __init__(self):
        super(Navegador, self).__init__()
        main_container = QVBoxLayout()
        hbox = QHBoxLayout()
        btn_atras = QPushButton(QIcon.fromTheme("back"), "Atras")
        btn_adelante = QPushButton(QIcon.fromTheme("forward"), "Adelante")
        btn_ok = QPushButton(QIcon.fromTheme("find"), "Buscar")
        btn_ok.setObjectName("ok")
        btn_actualizar = QPushButton(QIcon.fromTheme("reload"), "Actualizar")
        btn_stop = QPushButton(QIcon.fromTheme("cancel"), "")
        self.url = QLineEdit()

        hbox.addWidget(btn_atras)
        hbox.addWidget(btn_adelante)
        hbox.addWidget(btn_stop)
        hbox.addWidget(btn_actualizar)
        hbox.addWidget(self.url)
        hbox.addWidget(btn_ok)

        main_container.addLayout(hbox)
        self.setLayout(main_container)

        self.web = QWebView()
        main_container.addWidget(self.web)

        self.status = QStatusBar()
        self.progress = QProgressBar()
        self.status.addWidget(self.progress)
        self.status.addWidget(QLabel("Cargando.."))
        main_container.addWidget(self.status)

        btn_atras.clicked.connect(self.web.back)
        btn_adelante.clicked.connect(self.web.forward)
        btn_stop.clicked.connect(self.web.stop)
        btn_actualizar.clicked.connect(self.web.reload)
        self.url.returnPressed.connect(self.cargar_pagina)
        self.web.loadProgress.connect(self.progress.setValue)

    def cargar_pagina(self):
        text = self.url.text()
        if text.find('.') != -1 and not text.startswith('http://'):
            url = 'http://' + text
        else:
            url = 'http://google.com/search?q=' + text.replace(' ', '+')
        self.web.load(QUrl(url))


if __name__ == "__main__":
    app = QApplication([])
    w = Navegador()
    with open('style.qss') as f:
        app.setStyleSheet(f.read())
    w.show()
    app.exec_()
