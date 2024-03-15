from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLineEdit, QLabel

class button(QPushButton):
    def __init__(self, caption: str, window: QWidget) -> None:
        super().__init__(caption, window)
        self.clicked.connect(self.pressed)
        self.setStyleSheet('font-size: 18px')
        global check
        check = False

    def pressed(self):
        global input1, check
        condition = ''
        if self.text() == '=':
            if input1.text()[-1] in '*-/+':
                input1.setText(input1.text()[:-1])
            condition += str(eval(input1.text()))
            input1.setText(condition)
            check = True
        elif self.text() == '←':
            condition = input1.text()[:-1]
            input1.setText(condition)
        else:
            if check:
                if self.text() not in '*/+-':
                    input1.clear()
                check = False
        
            print(self.text(), end=' ')
            condition = input1.text()
            condition += self.text()
            input1.setText(condition)

            if len(input1.text()) > 2 and input1.text()[-1] in '/*-+' and input1.text()[-2] in '/*-+':
                condition = input1.text()
                condition = condition[:-2] + self.text()
                input1.setText(condition)


class Input(QLineEdit):
    def __init__(self, window: QWidget, placeholder: str) -> None:
        super().__init__(window)
        self.setPlaceholderText(placeholder)
        self.setStyleSheet('border: 0px; font-size: 18px')

class lablel(QLabel):
    def __init__(self, window: QWidget):
        super().__init__(window)
        self.adjustSize()
        self.setText('History is clear!')
        self.setStyleSheet('font-size: 18px')
 
calculator = QApplication([])
window = QWidget()
window.setWindowTitle('Calculator')
window.setFixedSize(395, 330)
window.setGeometry(920, 300, 395, 330)
history_pan = lablel(window)

history_pan.setGeometry(10, 10, 200, 30)

clear_element = button('←', window)
clear_element.setGeometry(295, 45, 90, 50)

one = button('1', window)
two = button('2', window)
three = button('3', window)
divide = button('/', window)

one.setGeometry(10, 100, 90, 50)
two.setGeometry(105, 100, 90, 50)
three.setGeometry(200, 100, 90, 50)
divide.setGeometry(295, 100, 90, 50)

four = button('4', window)
five = button('5', window)
six = button('6', window)
multiply = button('*', window)

four.setGeometry(10, 155, 90, 50)
five.setGeometry(105, 155, 90, 50)
six.setGeometry(200, 155, 90, 50)
multiply.setGeometry(295, 155, 90, 50)

seven = button('7', window)
eight = button('8', window)
nine = button('9', window)
minus = button('-', window)

seven.setGeometry(10, 210, 90, 50)
eight.setGeometry(105, 210, 90, 50)
nine.setGeometry(200, 210, 90, 50)
minus.setGeometry(295, 210, 90, 50)

zero = button('0', window)
equal = button('=', window)
plus = button('+', window)

zero.setGeometry(10, 265, 121, 50)
equal.setGeometry(138, 265, 121, 50)
plus.setGeometry(265, 265, 121, 50)


global input1
input1 = Input(window, '0') 
input1.setGeometry(10, 60, 280, 35)

window.show()
calculator.exec_()
