import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QLabel, QTabWidget,QVBoxLayout,QLineEdit,QPushButton,QMessageBox
from PyQt5.QtCore import *
import Alumno

class Principal(QMainWindow):
    #constructor de la clase principal
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Menú")
        self.setGeometry(100, 100, 600, 300)
        self.layout = QVBoxLayout(self)
        self.tabs = QTabWidget(self)
        self.tabs.resize(400, 250)
        self.setCentralWidget(self.tabs)

        self.tab_registro= QWidget()
        self.tab_test= QWidget()
        self.tab_res= QWidget()


        self.tabs.addTab(self.tab_registro, "Registro")
        self.tabs.addTab(self.tab_test, "Test")
        self.tabs.addTab(self.tab_res, "Resultados")

        self.crear_pestana_registro()
        self.crear_pestana_test()
        self.crear_pestana_resultados()

    def crear_pestana_registro(self):
         # Crea los diferentes widgets
        self.lb_nombre = QLabel("Nombre")
        self.lb_correo = QLabel("Correo electronico")
        self.lb_edad = QLabel("Edad")
        self.txt_nombre = QLineEdit()
        self.txt_correo = QLineEdit()
        self.txt_edad = QLineEdit()


        self.btn_registro = QPushButton("Registro")

        # Crea el layout y los agrega en la coordenada deseada
        layout = QGridLayout()
        layout.addWidget(self.lb_nombre, 0, 0)
        layout.addWidget(self.txt_nombre, 0, 1)
        layout.addWidget(self.lb_correo, 1, 0)
        layout.addWidget(self.txt_correo, 1, 1)
        layout.addWidget(self.lb_edad, 2, 0)
        layout.addWidget(self.txt_edad, 2, 1)
        layout.addWidget(self.btn_registro, 3, 2)

        self.tab_registro.setLayout(layout)
        
        self.btn_registro.clicked.connect(self.registro)

    def crear_pestana_test(self):
        layout = QGridLayout()
        etiqueta2 = QLabel("Test")
        layout.addWidget(etiqueta2, 0, 0)
        self.tab_test.setLayout(layout)

    def crear_pestana_resultados(self):
        layout = QGridLayout()
        etiqueta3 = QLabel("Resultados")
        layout.addWidget(etiqueta3, 0, 0)
        self.tab_res.setLayout(layout)

    def registro (self):
        try:
            self.edad = float(self.txt_edad.text())
            
        except:
            QMessageBox.warning(self,"error","ingresa solo numeros")
    
# Ejecuta la apessageBox.warning(self, "Error", "Por favor, ingresa un número válido.")

        else:
            nombre=self.txt_nombre.text()
            correo=self.txt_correo.text()
            edad=self.txt_edad.text()

            estudiante = Alumno(nombre,correo,edad)
            QMessageBox.warning(self,"el usuario se registro correctamente")

            self.licación

app = QApplication(sys.argv)
window = Principal()
window.show()
sys.exit(app.exec_())