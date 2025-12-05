import sys
from PyQt5.QtWidgets import QMainWindow, QGridLayout, QWidget, QApplication, QLabel, QLineEdit, QPushButton,QRadioButton
from Pregunta import Pregunta

class Principal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Test")
        #crear las preguntas y las asigna al cuestionario
        self.crearCuestionario()
        #indica la posicion en la que inicia el cuestionario
        self.index=0
        #indica la ultima posicion del cuestionario
        self.maximo= len(self.cuestionario)

        #Crea los diferentes widgets
        self.lb_num= QLabel("numero de pregunta")
        self.lb_pregunta= QLabel("pregunta")
        self.btn_siguiente= QPushButton("siguiente")
        self.btn_op1=QRadioButton("Siempre")
        self.btn_op2=QRadioButton("Aveces")
        self.btn_op3=QRadioButton("Frecuentemente")
        self.btn_op4=QRadioButton("Nunca")
        

        #Crea el layout y los agrega en la coordenada deseada
        layout = QGridLayout()
        layout.addWidget(self.lb_num,0,0)
        layout.addWidget(self.lb_pregunta,1,0)
        layout.addWidget(self.btn_op1,2,0)
        layout.addWidget(self.btn_op2,3,0)
        layout.addWidget(self.btn_op3,4,0)
        layout.addWidget(self.btn_op4,5,0)
        layout.addWidget(self.btn_siguiente,6,0)

        
    

        #Crea los eventos
        self.btn_siguiente.clicked.connect(self.siguiente)

        #Agrega el layout a la ventana
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


    def crearCuestionario(self):
        #Creación de objetos
        #se crea los objetos 
        pregunta1 = Pregunta (1, "¿Con que frecuencia tomas fotografías en un día normal?",0)
        pregunta2 = Pregunta (2, "¿Sientes ansiedad si no puedes usar tu cámara o telefono para tomar fotos?",0)
        pregunta3 = Pregunta (3, "¿Subes tus fotos a redes sociales inmediatamente despúes de tomarlas?",0)
        pregunta4 = Pregunta (4, "¿Has recibido comentarios de que tomas demasiadas fotos?",0)
        pregunta5 = Pregunta (5, "¿Te cuesta disfrutar momentos sin tomar fotos?",0)
        pregunta6 = Pregunta (6, "¿Con que frecuencia sientes la necesidad de tomar fotos en cualquier lugar o momento?",0)
        pregunta7 = Pregunta (7, "¿Que haces cuando no puedes tomar una foto en una situacion que te gustaria capturar?",0)
        pregunta8 = Pregunta (8, "¿Revisas constantemente las fotos que tomas para publicarlas en redes sociales?",0)
        pregunta9 = Pregunta (9, "¿Tomas fotos para conservar recuerdos o mas bien para btener aprobacion de los demas (likes, comentarios)?",0)
        pregunta10 = Pregunta (10, "¿Has dejado de disfrutar un momento porque estabas concentrado en tomar la foto perfecta?",0)

        #se agregan las preguntas a la lista
        self.cuestionario = [pregunta1,pregunta2,pregunta3,pregunta4,pregunta5,pregunta6,pregunta7,pregunta8,pregunta9,pregunta10]


    def siguiente(self):
        num=str(self.cuestionario[self.index].num_pregunta)
        preg=self.cuestionario[self.index].texto
        self.lb_num.setText(num)
        self.lb_pregunta.setText(preg)

        if(self.index < self.maximo-1):
            self.index= self.index +1


app= QApplication(sys.argv)
window= Principal()
window.show()
app.exec_()