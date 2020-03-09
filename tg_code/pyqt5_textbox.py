import sys 
from PyQt5.QtWidgets import QMainWindow,QApplication,QPushButton,QLineEdit

class App(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Тест")
		self.setGeometry(10, 10, 400, 140)
		# Создать textbox 
		self.textbox = QLineEdit(self) # Создать текстовый ввод
		self.textbox.move(20, 20)
		self.textbox.resize(280,40)
		# Создать кнопку в окне
		self.button = QPushButton('Показать',self)
		self.button.move(20,80)

		# Подключите кнопку к функции on_click
		self.button.clicked.connect(self.on_click)
		self.show()
	def on_click(self):
		text = self.textbox.text() # Получить текст
		print("Текст : ", text)	# принтить
		self.textbox.setText("") # Очистить текст

app = QApplication(sys.argv)	
ex = App()
sys.exit(app.exec_())	
