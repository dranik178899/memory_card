from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QMessageBox, QRadioButton, QGroupBox

app = QApplication([])
win = QWidget()



question = QLabel("Какой национальности не существует?")
question1 = QLabel("Варианты ответов")
v1 = QRadioButton("Энцы")
v2 = QRadioButton("Смурфы")
v3 = QRadioButton("Чулымцы")
v4 = QRadioButton("Алеуты")
Button = QPushButton("Отаветить")

RadioGroupBox = QGroupBox("Варианты ответов")
AnsGroupBox = QGroupBox("отавета")
otaveta = QLabel('Аулеты')

lay0 = QVBoxLayout()
lay1 = QHBoxLayout()
lay2 = QVBoxLayout()
lay3 = QVBoxLayout()
layotaveta = QHBoxLayout()
 
lay2.addWidget(v1)
lay2.addWidget(v2)
lay3.addWidget(v3)
lay3.addWidget(v4)
lay1.addLayout(lay2)
lay1.addLayout(lay3)
lay0.addWidget(question)
lay0.addWidget(RadioGroupBox)
lay0.addWidget(AnsGroupBox)
lay0.addWidget(Button)
layotaveta.addWidget(otaveta)

RadioGroupBox.setLayout(lay1)
AnsGroupBox.setLayout(layotaveta)
AnsGroupBox.hide()

lay0.addStretch(1)
lay0.addWidget(Button, stretch=2)
lay0.addStretch(1)



anslabel = QLabel('Отавета')

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    Button.setText("Следующий вопороса")

def show_Question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    Button.setText("Отаветить")



def start_test():
    #если текст на БУТТОН ответить то функция схоу резулт
    #если текст на буттон следующий вопроса то функция схоу квестион
    if Button.text() == "Отаветить":
        show_result()
    else:
        show_Question()

Button.clicked.connect(start_test)

# question.setText("Гос язык Бразилии")
# v1.setText("Португальский")
# v2.setText("Испанский")
# v3.setText("Итальянский")
# v4.setText("Бразильский")

win.setLayout(lay0)#лэйаут с лэйаутами ToD)
win.show()
app.exec_()
