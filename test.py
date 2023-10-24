import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QPushButton, QTableWidget, QTableWidgetItem
from random import sample

class HorarioEscolarApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Generador de Horarios Escolares')
        self.setGeometry(100, 100, 800, 600)

        layout = QVBoxLayout()

        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(5)
        self.tableWidget.setColumnCount(5)
        layout.addWidget(self.tableWidget)

        generate_button = QPushButton('Generar Horario')
        generate_button.clicked.connect(self.generate_horario)
        layout.addWidget(generate_button)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def generate_horario(self):
        # Simulación de generación de horario
        profesores = ['Profesor A', 'Profesor B', 'Profesor C', 'Profesor D', 'Profesor E']
        materias = ['Materia 1', 'Materia 2', 'Materia 3', 'Materia 4', 'Materia 5']

        horario = sample(profesores, len(profesores))
        horario = [horario[i:i+5] for i in range(0, len(horario), 5)]

        for i, row in enumerate(horario):
            for j, item in enumerate(row):
                self.tableWidget.setItem(i, j, QTableWidgetItem(item))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = HorarioEscolarApp()
    ex.show()
    sys.exit(app.exec_())
