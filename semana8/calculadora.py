import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QComboBox, QMessageBox, QVBoxLayout, QHBoxLayout

class CalculadoraIMC(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculadora de IMC - PyQt5")
        self.setGeometry(200, 200, 400, 300)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Nombre
        self.lbl_nombre = QLabel("Nombre:")
        self.entry_nombre = QLineEdit()
        layout.addWidget(self.lbl_nombre)
        layout.addWidget(self.entry_nombre)

        # Peso
        self.lbl_peso = QLabel("Peso:")
        h_peso = QHBoxLayout()
        self.entry_peso = QLineEdit()
        self.combo_peso = QComboBox()
        self.combo_peso.addItems(["kg", "lb"])
        h_peso.addWidget(self.entry_peso)
        h_peso.addWidget(self.combo_peso)
        layout.addWidget(self.lbl_peso)
        layout.addLayout(h_peso)

        # Altura
        self.lbl_altura = QLabel("Altura:")
        h_altura = QHBoxLayout()
        self.entry_altura = QLineEdit()
        self.combo_altura = QComboBox()
        self.combo_altura.addItems(["m", "cm"])
        h_altura.addWidget(self.entry_altura)
        h_altura.addWidget(self.combo_altura)
        layout.addWidget(self.lbl_altura)
        layout.addLayout(h_altura)

        # Botones
        h_botones = QHBoxLayout()
        self.btn_calcular = QPushButton("Calcular IMC")
        self.btn_calcular.clicked.connect(self.calcular_imc)
        self.btn_limpiar = QPushButton("Limpiar")
        self.btn_limpiar.clicked.connect(self.limpiar)
        h_botones.addWidget(self.btn_calcular)
        h_botones.addWidget(self.btn_limpiar)
        layout.addLayout(h_botones)

        # Resultado
        self.lbl_resultado = QLabel("")
        layout.addWidget(self.lbl_resultado)

        self.setLayout(layout)

    def calcular_imc(self):
        try:
            nombre = self.entry_nombre.text()
            peso = float(self.entry_peso.text())
            altura = float(self.entry_altura.text())

            # Convertir unidades si es necesario
            if self.combo_peso.currentText() == "lb":
                peso *= 0.453592  # lb → kg
            if self.combo_altura.currentText() == "cm":
                altura /= 100  # cm → m

            if altura <= 0:
                raise ValueError("La altura debe ser mayor que cero")

            # Calcular IMC
            imc = peso / (altura ** 2)
            if imc < 18.5:
                categoria = "Bajo peso"
            elif imc < 25:
                categoria = "Normal"
            elif imc < 30:
                categoria = "Sobrepeso"
            else:
                categoria = "Obesidad"

            self.lbl_resultado.setText(f"{nombre}, tu IMC es {imc:.2f} ({categoria})")

        except ValueError:
            QMessageBox.warning(self, "Error", "Ingresa números válidos para peso y altura")

    def limpiar(self):
        self.entry_nombre.clear()
        self.entry_peso.clear()
        self.entry_altura.clear()
        self.combo_peso.setCurrentIndex(0)
        self.combo_altura.setCurrentIndex(0)
        self.lbl_resultado.setText("")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CalculadoraIMC()
    window.show()
    sys.exit(app.exec_())

