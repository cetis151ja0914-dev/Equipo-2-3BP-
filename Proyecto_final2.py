import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QLabel, QTabWidget, QVBoxLayout, QLineEdit, QPushButton, QMessageBox, QGroupBox, QRadioButton, QHBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from Pregunta import Pregunta
from Alumno import Alumno

# Gráfica
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

#  ESTILOS
estilos = """
QMainWindow {
    background-color: #E773E2;
}
QWidget {
    background-color: #7690CC;   
}
QLabel {
    font-size: 14px;
}

QLineEdit {
    border: 2px solid #09133E;
    border-radius: 5px;
    padding: 4px;
    background-color: white;
}

QPushButton {
    background-color: #1B38B6;
    color: white;
    border-radius: 6px;
    padding: 6px 10px;
}
QPushButton:hover {
    background-color: #99A9F0;
}
QPushButton:pressed {
    background-color: #1B38B6;
}

QGroupBox {
    font-weight: bold;
    border: 1px solid #888;
    border-radius: 6px;
    margin-top: 10px;
    padding: 10px;
}

QRadioButton {
    font-size: 13px;
    margin: 3px;
}
"""


# CLASE PRINCIPAL 
class Principal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Detección de adicción a tomar fotografías")
        self.setGeometry(100, 100, 1000, 650)

        # Tabs principales
        self.tabs = QTabWidget(self)
        self.setCentralWidget(self.tabs)

        # Crear pestañas
        self.tab_bienvenida = QWidget()
        self.tab_registro = QWidget()
        self.tab_test = QWidget()
        self.tab_res = QWidget()

        self.tabs.addTab(self.tab_bienvenida, "Bienvenida")
        self.tabs.addTab(self.tab_registro, "Registro")
        self.tabs.addTab(self.tab_test, "Test")
        self.tabs.addTab(self.tab_res, "Resultados")

        # Crear contenido
        self.crear_bienvenida()
        self.crearCuestionario()
        self.crear_pestana_registro()
        self.crear_pestana_test()
        self.crear_pestana_resultados()

    # BIENVENIDA 
    def crear_bienvenida(self):
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)

        titulo = QLabel("¡Bienvenido al software de detección de adicción a tomar fotografías!")
        titulo.setStyleSheet("font-size:22px; font-weight:bold;")
        layout.addWidget(titulo, alignment=Qt.AlignCenter)

        imagen = QLabel()
        pix = QPixmap("descarga.png")
        pix = pix.scaled(350, 230)
        imagen.setPixmap(pix)
        layout.addWidget(imagen, alignment=Qt.AlignCenter)

        texto = QLabel(
        "Este test tiene como propósito evaluar los niveles de dependencia o\n"
        "adicción a tomar fotografías, permitiendo reconocer si esta práctica\n"
        "se realiza por gusto, necesidad o hábito. Los resultados servirán para\n"
        "fomentar el autocontrol y el uso responsable de la tecnología."
    )
        texto.setStyleSheet("font-size:16px;")
        texto.setAlignment(Qt.AlignCenter)
        layout.addWidget(texto, alignment=Qt.AlignCenter)

        # BOTÓN CONTINUAR (solo cambia de pestaña)
        self.btn_continuar = QPushButton("Continuar")
        self.btn_continuar.setFixedWidth(150)
        self.btn_continuar.clicked.connect(lambda: self.tabs.setCurrentIndex(1))
        layout.addWidget(self.btn_continuar, alignment=Qt.AlignCenter)

        self.tab_bienvenida.setLayout(layout)

    # REGISTRO 
    def crear_pestana_registro(self):

        # Etiquetas
        self.lb_nombre = QLabel("Nombre")
        self.lb_correo = QLabel("Correo electrónico")
        self.lb_edad = QLabel("Edad")

        # Cajas de texto
        self.txt_nombre = QLineEdit()
        self.txt_correo = QLineEdit()
        self.txt_edad = QLineEdit()

        # Botón Registrar
        self.btn_registro = QPushButton("Registrar")
        self.btn_registro.setFixedWidth(150)  # mismo tamaño

        # Botón Continuar (MISMO tamaño que Registrar)
        self.btn_continuar_reg = QPushButton("Continuar")
        self.btn_continuar_reg.setFixedWidth(150)
        self.btn_continuar_reg.clicked.connect(lambda: self.tabs.setCurrentIndex(2))

        # Layout de registro
        layout = QGridLayout()
        layout.addWidget(self.lb_nombre, 0, 0)
        layout.addWidget(self.txt_nombre, 0, 1)
        layout.addWidget(self.lb_correo, 1, 0)
        layout.addWidget(self.txt_correo, 1, 1)
        layout.addWidget(self.lb_edad, 2, 0)
        layout.addWidget(self.txt_edad, 2, 1)

        # Ambos botones alineados
        botones = QHBoxLayout()
        botones.addWidget(self.btn_registro)
        botones.addWidget(self.btn_continuar_reg)

        layout.addLayout(botones, 3, 0, 1, 2)

        self.tab_registro.setLayout(layout)
        self.btn_registro.clicked.connect(self.registro)

    def registro(self):
        # Guardar textos
        nombre = self.txt_nombre.text().strip()
        correo = self.txt_correo.text().strip()
        edad_txt = self.txt_edad.text().strip()

        # Validar campos vacíos
        if nombre == "" or correo == "" or edad_txt == "":
            QMessageBox.warning(self, "Campos obligatorios", "Todos los campos de registro son obligatorios.")
            return

        # Validar edad numérica
        try:
            edad = int(edad_txt)
        except:
            QMessageBox.warning(self, "Error", "Ingresa solo números en edad")
            return

        # Registro correcto
        QMessageBox.information(self, "Correcto", "El usuario se registró correctamente")
        Alumno(nombre, correo, edad)
        print(nombre, correo, edad)

    # CUESTIONARIO 
    def crearCuestionario(self):
        self.cuestionario = [
            Pregunta(1, "¿Con qué frecuencia tomas fotografías durante tu día?", 0),
            Pregunta(2, "¿Qué tan seguido sientes ansiedad por no poder tomar una foto?", 0),
            Pregunta(3, "¿Subes tus fotos a redes sociales inmediatamente?", 0),
            Pregunta(4, "¿Te dicen que tomas demasiadas fotos?", 0),
            Pregunta(5, "¿Te cuesta disfrutar momentos sin tomar una foto?", 0),
            Pregunta(6, "¿Necesitas tomar fotos en cualquier lugar?", 0),
            Pregunta(7, "¿Te afecta no poder tomar foto cuando quieres?", 0),
            Pregunta(8, "¿Revisas tus fotos constantemente?", 0),
            Pregunta(9, "¿Tomas fotos buscando aprobación?", 0),
            Pregunta(10, "¿Pierdes concentración buscando la foto perfecta?", 0),
        ]

    # TEST 
    def crear_pestana_test(self):
        self.index = 0
        self.maximo = len(self.cuestionario)
        
        cont_pregunta= QVBoxLayout()
        self.lb_num_pregunta = QLabel(str(self.cuestionario[self.index].num_pregunta))
        self.lb_texto = QLabel(self.cuestionario[self.index].texto)

        self.lb_num_pregunta.setStyleSheet("font-size:18px; font-weight:bold;")
        self.lb_texto.setStyleSheet("font-size:16px;")

        cont_pregunta.addWidget(self.lb_num_pregunta)
        cont_pregunta.addWidget(self.lb_texto)

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

        self.btn_siguiente = QPushButton("Siguiente")
        self.btn_siguiente.clicked.connect(self.siguiente)

        layout = QGridLayout()
        layout.addLayout(cont_pregunta, 0, 0)
        layout.addWidget(self.grupo, 1, 0)
        layout.addWidget(self.btn_siguiente, 2, 0)     

        self.tab_test.setLayout(layout)

    def validar_respuesta(self):
        if self.btn_op1.isChecked(): return 0
        if self.btn_op2.isChecked(): return 1
        if self.btn_op3.isChecked(): return 2
        if self.btn_op4.isChecked(): return 3
        return -1

    def siguiente(self):
        valor = self.validar_respuesta()

        if valor == -1:
            QMessageBox.warning(self, "Error", "Selecciona una opción")
            return

        self.cuestionario[self.index].respuesta = valor
        self.index += 1

        if self.index < self.maximo:
            p = self.cuestionario[self.index]
            self.lb_num_pregunta.setText(str(p.num_pregunta))
            self.lb_texto.setText(p.texto)
            self.btn_op1.setChecked(False)
            self.btn_op2.setChecked(False)
            self.btn_op3.setChecked(False)
            self.btn_op4.setChecked(False)
        else:
            QMessageBox.information(self, "Fin", "Has terminado el test.")
            self.mostrar_resultados()
            self.tabs.setCurrentIndex(3)

    #  RESULTADOS 
    def crear_pestana_resultados(self):
        layout = QVBoxLayout()

        self.lb_res = QLabel("Aquí aparecerán los resultados")
        layout.addWidget(self.lb_res)

        #recomendacion
        self.lb_nivel = QLabel("")           
        self.lb_recomendacion = QLabel("")   
        layout.addWidget(self.lb_nivel)     
        layout.addWidget(self.lb_recomendacion)  

        # Gráfica
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        layout.addWidget(self.canvas)

        self.tab_res.setLayout(layout)

    def mostrar_resultados(self):
        texto = ""
        for p in self.cuestionario:
            texto += f"Pregunta {p.num_pregunta}: {p.respuesta}\n"
        self.lb_res.setText(texto)

        valores = [p.respuesta for p in self.cuestionario]

        #nivel y recomendación
        puntaje = sum(valores)
        if puntaje <= 10:
            nivel = "BAJO"
            recomendacion = "Bajo control, sigue así."
        elif puntaje <= 20:
            nivel = "MODERADO"
            recomendacion = "Controla tus tiempos y evita el exceso."
        else:
            nivel = "ALTO"
            recomendacion= "Podría afectar tu bienestar, busca ayuda profesional."

        self.lb_nivel.setText(f"Nivel de adicción: {nivel} ({puntaje} puntos)")
        self.lb_recomendacion.setText(f"Recomendación: {recomendacion}")

        self.figure.clear()
        ax = self.figure.add_subplot(111)

        labels = ["Nunca", "A veces", "Frecuente", "Siempre"]
        conteo = [
            valores.count(0),
            valores.count(1),
            valores.count(2),
            valores.count(3)
        ]
        #Grafica de pastel
        ax.pie(conteo, labels=labels, autopct="%1.1f%%", startangle=90)
        ax.set_title("Distribución de respuestas")

        #Muestra la leyenda
        ax.legend(labels, loc="center left", bbox_to_anchor=(1.1, 0.5))
        ax.set_position([0.05, 0.1, 0.6, 0.8])
        # Dibujar la gráfica en el canvas del widgetq

        self.canvas.draw()

# Esta línea verifica si este archivo se está ejecutando directamente.
# Si es así, se ejecuta el código dentro del bloque.
# Sirve para evitar que ese código se ejecute cuando el archivose importa desde otro módulo.
if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(estilos)
    ventana = Principal()
    ventana.show()
    sys.exit(app.exec_())
