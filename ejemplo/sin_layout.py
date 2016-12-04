from PyQt5.QtWidgets import *


if __name__ == "__main__":
    app = QApplication([])
    v = QWidget()
    v.resize(400, 300)
    b = QPushButton("Botón", v)
    b2 = QPushButton("Otro Botón", v)
    b.move(100, 200)
    b2.move(250, 200)
    v.show()
    app.exec_()
