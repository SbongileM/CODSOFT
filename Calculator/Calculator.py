'''
Author: Sbongile Mdaki
Date:  22 January 2023
Project: GUI desktop calculator application for CodSoft internship

This project aims to create a simple calculator with basic arithmetic operations using python.
The calculator prompts the user to input two numbers and an operation of choice, performs a 
calculation and then displays the result.

'''
from PyQt5 import QtCore, QtGui, QtWidgets

class WindowSetup():
    def __init__(self, window):
        super().__init__()
        
        #Window settings
        window.setWindowTitle("Calculator")
        window.setMaximumSize(600,500)
        window.resize(300,500)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icons/window icon.png"))
        window.setWindowIcon(icon)
        self.central_widget = QtWidgets.QWidget(window)
        
        #Layout settings
        #window layout
        self.vertical_layout = QtWidgets.QVBoxLayout(self.central_widget)
        #buttons layouts
        self.horizontal_layout = QtWidgets.QHBoxLayout()
        self.horizontal_layout_2 = QtWidgets.QHBoxLayout()
        self.horizontal_layout_3 = QtWidgets.QHBoxLayout()
        self.horizontal_layout_4 = QtWidgets.QHBoxLayout()
        self.horizontal_layout_5 = QtWidgets.QHBoxLayout()
        self.horizontal_layout_6 = QtWidgets.QHBoxLayout()
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        
        #Calculator screen font settings
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        
        #Calculator screen settings
        self.screen = QtWidgets.QLabel("Click on two numbers and an operation")
        self.screen.setSizePolicy(size_policy)
        self.screen.setFont(font)
        self.screen.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.screen.setFrameShape(QtWidgets.QFrame.Box)
        self.screen.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
        self.vertical_layout.addWidget(self.screen)
        
        #Buttons font settings
        style = "font: 63 12pt \"Segoe UI Semibold\";"

        #Reset button settings
        self.clear = QtWidgets.QPushButton("C")
        self.clear.setSizePolicy(size_policy)
        self.clear.setStyleSheet(style)
        self.horizontal_layout.addWidget(self.clear)
        
        #Left hand parethesis settings
        self.Lparenthesis = QtWidgets.QPushButton("(")
        self.Lparenthesis.setSizePolicy(size_policy)
        self.Lparenthesis.setStyleSheet(style)
        self.horizontal_layout.addWidget(self.Lparenthesis)
        
        #Right hand parenthesis settings
        self.Rparenthesis = QtWidgets.QPushButton(")")
        self.Rparenthesis.setSizePolicy(size_policy)
        self.Rparenthesis.setStyleSheet(style)
        self.horizontal_layout.addWidget(self.Rparenthesis)
        
        #Percentage button settings
        self.percentage = QtWidgets.QPushButton("%")
        self.percentage.setSizePolicy(size_policy)
        self.percentage.setStyleSheet(style)
        self.horizontal_layout.addWidget(self.percentage)
        
        self.vertical_layout.addLayout(self.horizontal_layout)
        
        #Delete button settings
        self.back_space = QtWidgets.QPushButton("<x]")
        self.back_space.setSizePolicy(size_policy)
        self.back_space.setStyleSheet(style)
        self.horizontal_layout_2.addWidget(self.back_space)
        
        #Square button settings
        self.square = QtWidgets.QPushButton("x^2")
        self.square.setSizePolicy(size_policy)
        self.square.setStyleSheet(style)
        self.horizontal_layout_2.addWidget(self.square)
        
        #Square root button settings
        self.root = QtWidgets.QPushButton("√x ")
        self.root.setSizePolicy(size_policy)
        self.root.setStyleSheet(style)
        self.horizontal_layout_2.addWidget(self.root)
        
        #Division button settings
        self.division = QtWidgets.QPushButton("÷")
        self.division.setSizePolicy(size_policy)
        self.division.setStyleSheet(style)
        self.horizontal_layout_2.addWidget(self.division)
        
        self.vertical_layout.addLayout(self.horizontal_layout_2)
        
        #Number 7 button settings
        self.seven = QtWidgets.QPushButton("7")
        self.seven.setSizePolicy(size_policy)
        self.seven.setStyleSheet(style)
        self.horizontal_layout_3.addWidget(self.seven)
        
        #Number 8 button settings
        self.eight = QtWidgets.QPushButton("8")
        self.eight.setSizePolicy(size_policy)
        self.eight.setStyleSheet(style)
        self.horizontal_layout_3.addWidget(self.eight)
        
        #Number 9 button settings
        self.nine = QtWidgets.QPushButton("9")
        self.nine.setSizePolicy(size_policy)
        self.nine.setStyleSheet(style)
        self.horizontal_layout_3.addWidget(self.nine)
        
        #Multiplication button settings
        self.multiplication = QtWidgets.QPushButton("×")
        self.multiplication.setSizePolicy(size_policy)
        self.multiplication.setStyleSheet(style)
        self.horizontal_layout_3.addWidget(self.multiplication)
        
        self.vertical_layout.addLayout(self.horizontal_layout_3)
    
        #Number 4 button settings
        self.four = QtWidgets.QPushButton("4")
        self.four.setSizePolicy(size_policy)
        self.four.setStyleSheet(style)
        self.horizontal_layout_4.addWidget(self.four)
        
        #Number 5 button settings
        self.five = QtWidgets.QPushButton("5")
        self.five.setSizePolicy(size_policy)
        self.five.setStyleSheet(style)
        self.horizontal_layout_4.addWidget(self.five)
        
        #Number 6 button settings
        self.six = QtWidgets.QPushButton("6")
        self.six.setSizePolicy(size_policy)
        self.six.setStyleSheet(style)
        self.horizontal_layout_4.addWidget(self.six)
        
        #Subtraction button settings
        self.subtraction = QtWidgets.QPushButton("-")
        self.subtraction.setSizePolicy(size_policy)
        self.subtraction.setStyleSheet(style)
        self.horizontal_layout_4.addWidget(self.subtraction)
        
        self.vertical_layout.addLayout(self.horizontal_layout_4)
        
        #Number 3 button settings
        self.three = QtWidgets.QPushButton("3")
        self.three.setSizePolicy(size_policy)
        self.three.setStyleSheet(style)
        self.horizontal_layout_5.addWidget(self.three)
        
        #Number 2 button settings
        self.two = QtWidgets.QPushButton("2")
        self.two.setSizePolicy(size_policy)
        self.two.setStyleSheet(style)
        self.horizontal_layout_5.addWidget(self.two)
        
        #Number 1 button settings
        self.one = QtWidgets.QPushButton("1")
        self.one.setSizePolicy(size_policy)
        self.one.setStyleSheet(style)
        self.horizontal_layout_5.addWidget(self.one)
        
        #Addition button settings
        self.add = QtWidgets.QPushButton("+")
        self.add.setSizePolicy(size_policy)
        self.add.setStyleSheet(style)
        self.horizontal_layout_5.addWidget(self.add)
        
        self.vertical_layout.addLayout(self.horizontal_layout_5)
        
        #Plus or minus button settings
        self.negative_sign = QtWidgets.QPushButton("+/-")
        self.negative_sign.setSizePolicy(size_policy)
        self.negative_sign.setStyleSheet(style)
        self.horizontal_layout_6.addWidget(self.negative_sign)
        
        #Zero button settings
        self.zero = QtWidgets.QPushButton("0")
        self.zero.setSizePolicy(size_policy)
        self.zero.setStyleSheet(style)
        self.horizontal_layout_6.addWidget(self.zero)
        
        #Decimal point settings
        self.point = QtWidgets.QPushButton(".")
        self.point.setSizePolicy(size_policy)
        self.point.setStyleSheet(style)
        self.horizontal_layout_6.addWidget(self.point)
        
        #Equal sign settings
        self.equal = QtWidgets.QPushButton("=")
        self.equal.setSizePolicy(size_policy)
        self.equal.setStyleSheet("font: 63 12pt \"Segoe UI Semibold\";"
                                 "background-color: rgb(56, 199, 16);"
                                 "color: rgb(232, 232, 232);")
        self.horizontal_layout_6.addWidget(self.equal)
        
        self.vertical_layout.addLayout(self.horizontal_layout_6)
        
        window.setCentralWidget(self.central_widget)
        
        
    #General button functionality        
    def pressed(self, button):
        if button == "C":
            self.screen.setText("")
            
        elif self.screen.text() == "Click on two numbers and an operation":
            self.screen.setText(button)
        else:
            self.screen.setText(f'{self.screen.text()}{button}')
    
import Assets

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = WindowSetup(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
