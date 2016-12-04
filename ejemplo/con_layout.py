from PyQt5.QtWidgets import *


if __name__ == "__main__":
    app = QApplication([])
    v = QWidget()
    v.resize(400, 300)
    box = QHBoxLayout(v)
    b = QPushButton("Botón", v)
    b2 = QPushButton("Otro Botón", v)
    box.addWidget(b)
    box.addWidget(b2)
    v.show()
    app.exec_()
