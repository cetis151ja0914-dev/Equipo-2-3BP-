import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QLabel,QTabWidget, QVBoxLayout, QLineEdit, QPushButton, QMessageBox,QGroupBox, QRadioButton
from Pregunta import Pregunta
from Alumno import Alumno


class Principal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Menú")
        self.setGeometry(100, 100, 700, 350)

        # TABS
        self.tabs = QTabWidget(self)
        self.setCentralWidget(self.tabs)

        self.tab_registro = QWidget()
        self.tab_test = QWidget()
        self.tab_res = QWidget()

        self.tabs.addTab(self.tab_registro, "Registro")
        self.tabs.addTab(self.tab_test, "Test")
        self.tabs.addTab(self.tab_res, "Resultados")

        # crear cuestionario 
        self.crearCuestionario()

        # crear pestañas
        self.crear_pestana_registro()
        self.crear_pestana_test()
        self.crear_pestana_resultados()

    # Pestaña de registro
    def crear_pestana_registro(self):
        self.lb_nombre = QLabel("Nombre")
        self.lb_correo = QLabel("Correo electronico")
        self.lb_edad = QLabel("Edad")
        self.txt_nombre = QLineEdit()
        self.txt_correo = QLineEdit()
        self.txt_edad = QLineEdit()

        self.btn_registro = QPushButton("Registro")

        layout = QGridLayout()
        layout.addWidget(self.lb_nombre, 0, 0)
        layout.addWidget(self.txt_nombre, 0, 1)
        layout.addWidget(self.lb_correo, 1, 0)
        layout.addWidget(self.txt_correo, 1, 1)
        layout.addWidget(self.lb_edad, 2, 0)
        layout.addWidget(self.txt_edad, 2, 1)
        layout.addWidget(self.btn_registro, 3, 0)

        self.tab_registro.setLayout(layout)
        self.btn_registro.clicked.connect(self.registro)

    # crear cuestionario
    def crearCuestionario(self):
        # crea objetos Pregunta 
        self.cuestionario = [
            Pregunta(1, "¿Con que frecuencia tomas fotografías durante tu día?", 0),
            Pregunta(2, "¿Qué tan seguido sientes ansiedad por no poder tomar una fotografía cuando quieres?", 0),
            Pregunta(3, "¿Subes tus fotos a redes sociales inmediatamente después de tomarlas?", 0),
            Pregunta(4, "¿Qué tan seguido te dicen que tomas demasiadas fotos?", 0),
            Pregunta(5, "¿Te cuesta disfrutar momentos sin tomar una fotografía?", 0),
            Pregunta(6, "¿Con qué frecuencia sientes la necesidad de tomar fotos en cualquier lugar?", 0),
            Pregunta(7, "¿Qué tanto te afecta no poder tomar una foto cuando lo deseas?", 0),
            Pregunta(8, "¿Revisas constantemente tus fotos para publicarlas?", 0),
            Pregunta(9, "¿Con qué frecuencia tomas fotos buscando aprobación en redes?", 0),
            Pregunta(10, "¿Qué tan seguido pierdes concentración intentando tomar la foto perfecta?", 0),
        ]

    def crear_pestana_test(self):
        # índices y tamaño
        self.index = 0
        self.maximo = len(self.cuestionario)

        # Widgets del test (una sola vez)
        self.lb_num_pregunta = QLabel(str(self.cuestionario[self.index].num_pregunta))
        self.lb_texto = QLabel(self.cuestionario[self.index].texto)
        self.btn_siguiente = QPushButton("Siguiente")

        # RadioButtons
        self.grupo = QGroupBox("Selecciona una opción")
        vbox = QVBoxLayout()
        self.btn_op1 = QRadioButton("Nunca")
        self.btn_op2 = QRadioButton("A veces")
        self.btn_op3 = QRadioButton("Frecuentemente")
        self.btn_op4 = QRadioButton("Siempre")
        vbox.addWidget(self.btn_op1)
        vbox.addWidget(self.btn_op2)
        vbox.addWidget(self.btn_op3)
        vbox.addWidget(self.btn_op4)
        self.grupo.setLayout(vbox)

        # Layout del tab_test
        layout = QGridLayout()
        layout.addWidget(self.lb_num_pregunta, 0, 0)
        layout.addWidget(self.lb_texto, 1, 0)
        layout.addWidget(self.grupo, 2, 0)
        layout.addWidget(self.btn_siguiente, 3, 0)

        self.tab_test.setLayout(layout)
        self.btn_siguiente.clicked.connect(self.siguiente)

    def validar_respuesta(self):
     if self.btn_op1.isChecked():
        self.resp = 0
     elif self.btn_op2.isChecked():
        self.resp = 1
     elif self.btn_op3.isChecked():
        self.resp = 2
     elif self.btn_op4.isChecked():
        self.resp = 3
     else:
        QMessageBox.warning(self, "Error", "Seleccione una opción")
        self.resp = -1

    def siguiente(self):
        self.validar_respuesta()
        if self.resp == 1:
            return
        self.cuestionario[self.index].respuesta = self.resp #guarda respuesta
        self.index += 1
        if self.index < self.maximo:
            p = self.cuestionario[self.index]
            self.lb_num_pregunta.setText(str(p.num_pregunta))
            self.lb_texto.setText(p.texto)
    #limpia seleccion
            for b in [self.btn_op1, self.btn_op2, self.btn_op3, self.btn_op4]:
                b.setChecked(False)
        else :
            QMessageBox.information(self, "has terminado el test")
   


    # pestaña dd resultados
    def crear_pestana_resultados(self):
        layout = QGridLayout()
        layout.addWidget(QLabel("Resultados"), 0, 0)
        self.tab_res.setLayout(layout)

    # funcion registro
    def registro(self):
        # valida edad como entero
        try:
            edad = int(self.txt_edad.text())
        except Exception:
            QMessageBox.warning(self, "Error", "Ingresa solo números en edad")
            return

        nombre = self.txt_nombre.text()
        correo = self.txt_correo.text()

        # crea objeto Alumno (asegúrate que la clase Alumno usa estos parámetros)
        Alumno(nombre, correo, edad)
        QMessageBox.information(self, "Correcto", "El usuario se registró correctamente")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Principal()
    ventana.show()
    sys.exit(app.exec_())
