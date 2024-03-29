'''
Author: Sbongile Mdaki
Date:  22 January 2024
Project: GUI desktop calculator application for CodSoft internship

This project aims to create a simple calculator with basic arithmetic operations using python.
The calculator prompts the user to input two numbers and an operation of choice, performs a 
calculation and then displays the result.Additional functionalities such as percentage, square 
root,square and parenthesis were added.The calculator can evaluate more than just two numbers.
However, the functionality of the added operations is limited to only the current(one) number 
and does not work for an expression within a pair of parethesis. For example, sqrt(8+9).

'''

from re import findall as split
from PyQt5 import QtCore, QtGui, QtWidgets
import Assets

class WindowSetup():
    def __init__(self, window):
        super().__init__()
        
        #Window settings
        window.setWindowTitle("Calculator")
        window.setMaximumSize(500,500)
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
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, \
                                            QtWidgets.QSizePolicy.Preferred)
        
        #Calculator screen font settings
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        
        #Calculator screen settings
        self.screen = QtWidgets.QLabel("Click on two numbers and an operation")
        self.screen.setSizePolicy(size_policy)
        self.screen.setMaximumWidth(500)
        self.screen.setFont(font)
        self.screen.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.screen.setFrameShape(QtWidgets.QFrame.Box)
        self.screen.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
        self.vertical_layout.addWidget(self.screen)
        
        #Buttons font settings
        style = "font: 63 12pt \"Segoe UI Semibold\";"

        #Reset button settings
        self.clear = QtWidgets.QPushButton("C",clicked = lambda: self.pressed("C"))
        self.clear.setSizePolicy(size_policy)
        self.clear.setStyleSheet(style)
        self.horizontal_layout.addWidget(self.clear)
        
        #Left hand parethesis settings
        self.Lparenthesis = QtWidgets.QPushButton("(",clicked = lambda: self.pressed("("))
        self.Lparenthesis.setSizePolicy(size_policy)
        self.Lparenthesis.setStyleSheet(style)
        self.horizontal_layout.addWidget(self.Lparenthesis)
        
        #Right hand parenthesis settings
        self.Rparenthesis = QtWidgets.QPushButton(")",clicked = lambda: self.pressed(")"))
        self.Rparenthesis.setSizePolicy(size_policy)
        self.Rparenthesis.setStyleSheet(style)
        self.horizontal_layout.addWidget(self.Rparenthesis)
        
        #Percentage button settings
        self.percentage_ = QtWidgets.QPushButton("%",clicked = lambda: self.percent())
        self.percentage_.setSizePolicy(size_policy)
        self.percentage_.setStyleSheet(style)
        self.horizontal_layout.addWidget(self.percentage_)
        
        self.vertical_layout.addLayout(self.horizontal_layout)
        
        #Delete button settings
        self.back_space = QtWidgets.QPushButton("<x]",clicked = lambda: self.delete())
        self.back_space.setSizePolicy(size_policy)
        self.back_space.setStyleSheet(style)
        self.horizontal_layout_2.addWidget(self.back_space)
        
        #Square button settings
        self.square = QtWidgets.QPushButton("x^2",clicked = lambda: self.squared())
        self.square.setSizePolicy(size_policy)
        self.square.setStyleSheet(style)
        self.horizontal_layout_2.addWidget(self.square)
        
        #Square root button settings
        self.root = QtWidgets.QPushButton("√x ",clicked = lambda: self.sqroot())
        self.root.setSizePolicy(size_policy)
        self.root.setStyleSheet(style)
        self.horizontal_layout_2.addWidget(self.root)
        
        #Division button settings
        self.division = QtWidgets.QPushButton("÷",clicked = lambda: self.pressed("/"))
        self.division.setSizePolicy(size_policy)
        self.division.setStyleSheet(style)
        self.horizontal_layout_2.addWidget(self.division)
        
        self.vertical_layout.addLayout(self.horizontal_layout_2)
        
        #Number 7 button settings
        self.seven = QtWidgets.QPushButton("7",clicked = lambda: self.pressed("7"))
        self.seven.setSizePolicy(size_policy)
        self.seven.setStyleSheet(style)
        self.horizontal_layout_3.addWidget(self.seven)
        
        #Number 8 button settings
        self.eight = QtWidgets.QPushButton("8",clicked = lambda: self.pressed("8"))
        self.eight.setSizePolicy(size_policy)
        self.eight.setStyleSheet(style)
        self.horizontal_layout_3.addWidget(self.eight)
        
        #Number 9 button settings
        self.nine = QtWidgets.QPushButton("9",clicked = lambda: self.pressed("9"))
        self.nine.setSizePolicy(size_policy)
        self.nine.setStyleSheet(style)
        self.horizontal_layout_3.addWidget(self.nine)
        
        #Multiplication button settings
        self.multiplication = QtWidgets.QPushButton("×",clicked = lambda: self.pressed("*"))
        self.multiplication.setSizePolicy(size_policy)
        self.multiplication.setStyleSheet(style)
        self.horizontal_layout_3.addWidget(self.multiplication)
        
        self.vertical_layout.addLayout(self.horizontal_layout_3)
    
        #Number 4 button settings
        self.four = QtWidgets.QPushButton("4",clicked = lambda: self.pressed("4"))
        self.four.setSizePolicy(size_policy)
        self.four.setStyleSheet(style)
        self.horizontal_layout_4.addWidget(self.four)
        
        #Number 5 button settings
        self.five = QtWidgets.QPushButton("5",clicked = lambda: self.pressed("5"))
        self.five.setSizePolicy(size_policy)
        self.five.setStyleSheet(style)
        self.horizontal_layout_4.addWidget(self.five)
        
        #Number 6 button settings
        self.six = QtWidgets.QPushButton("6",clicked = lambda: self.pressed("6"))
        self.six.setSizePolicy(size_policy)
        self.six.setStyleSheet(style)
        self.horizontal_layout_4.addWidget(self.six)
        
        #Subtraction button settings
        self.subtraction = QtWidgets.QPushButton("-",clicked = lambda: self.pressed("-"))
        self.subtraction.setSizePolicy(size_policy)
        self.subtraction.setStyleSheet(style)
        self.horizontal_layout_4.addWidget(self.subtraction)
        
        self.vertical_layout.addLayout(self.horizontal_layout_4)
        
        #Number 3 button settings
        self.three = QtWidgets.QPushButton("3",clicked = lambda: self.pressed("3"))
        self.three.setSizePolicy(size_policy)
        self.three.setStyleSheet(style)
        self.horizontal_layout_5.addWidget(self.three)
        
        #Number 2 button settings
        self.two = QtWidgets.QPushButton("2",clicked = lambda: self.pressed("2"))
        self.two.setSizePolicy(size_policy)
        self.two.setStyleSheet(style)
        self.horizontal_layout_5.addWidget(self.two)
        
        #Number 1 button settings
        self.one = QtWidgets.QPushButton("1",clicked = lambda: self.pressed("1"))
        self.one.setSizePolicy(size_policy)
        self.one.setStyleSheet(style)
        self.horizontal_layout_5.addWidget(self.one)
        
        #Addition button settings
        self.add = QtWidgets.QPushButton("+",clicked = lambda: self.pressed("+"))
        self.add.setSizePolicy(size_policy)
        self.add.setStyleSheet(style)
        self.horizontal_layout_5.addWidget(self.add)
        
        self.vertical_layout.addLayout(self.horizontal_layout_5)
        
        #Plus or minus button settings
        self.negative_sign = QtWidgets.QPushButton("+/-",clicked = lambda: self.plus_minus())
        self.negative_sign.setSizePolicy(size_policy)
        self.negative_sign.setStyleSheet(style)
        self.horizontal_layout_6.addWidget(self.negative_sign)
        
        #Zero button settings
        self.zero = QtWidgets.QPushButton("0",clicked = lambda: self.pressed("0"))
        self.zero.setSizePolicy(size_policy)
        self.zero.setStyleSheet(style)
        self.horizontal_layout_6.addWidget(self.zero)
        
        #Decimal point settings
        self.point = QtWidgets.QPushButton(".",clicked = lambda: self.dec_point())
        self.point.setSizePolicy(size_policy)
        self.point.setStyleSheet(style)
        self.horizontal_layout_6.addWidget(self.point)
        
        #Equal sign settings
        self.equal = QtWidgets.QPushButton("=",clicked = lambda: self.calculate())
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
            
    #Evaluation function
    def calculate(self):
        input_txt = self.screen.text()
        try:
            answer = eval(input_txt)
            if len(str(answer)) > 4:
                self.screen.setText(str(format(answer,"e")))
            else:
                self.screen.setText(str(answer)) 
        except:
            self.screen.setText("ERROR")
            
    #Back space functionality
    def delete(self):
        self.screen.setText((self.screen.text())[:-1])
        
    #Extracts digits from the expression shown on the calculator screen
    #using a regular expression that removes the '+-*/' characters and stores
    #the digits into a list that can be traversed better than a string
    def split_up(self, input_):
        return split(r'\d+\.\d+|\d+|\.',input_)
    
    #Decimal point functionality
    def dec_point(self):
        try:
            if "." in self.split_up(self.screen.text())[-1]:
                pass
            else:
                self.screen.setText(f'{self.screen.text()}.')
        except:
            self.screen.setText("ERROR")
            
    #Negative/Positive
    #Waits for a number to be pressed first before it functions
    #Does not work for an expression within a set of (), only works for the current number
    def plus_minus(self):
        current_txt = self.screen.text()
        nums = self.split_up(current_txt)
        
        try:
            if len(nums) > 0 :
                current = nums[-1]
            
                if '-' in current_txt[-len(current)-1:] and current_txt[-1].isdigit():
                  
                    if len(nums) > 1 and current_txt[-len(current)-2].isdigit():
                        current_txt =current_txt.replace(current_txt[-len(current)-1],'+')
                    else:
                        current_txt = current_txt.replace(current_txt[-len(current)-1],'')
        
                elif current_txt[-1].isdigit():
                    current_txt = current_txt[:-len(current)] + '-' + current_txt[-len(current):]
                
            self.screen.setText(current_txt)
            
        except ValueError:
            self.screen.setText(current_txt)#do not make any changes
            
    #Percentage functionality  
    #Only works for the current number, not for an expression
    def percent(self):
        current_txt = self.screen.text()
        nums = self.split_up(current_txt)
        
        try:
            if nums[-1].isdecimal(): 
                num = int(nums[-1])
            else : 
                num = float(nums[-1])
            
            answer = num/100
            
            if current_txt[-1] in ')*/-+':
                self.screen.setText(current_txt)#do not make any changes
            else:
                i = -len(nums[-1])
                self.screen.setText(current_txt[:i]+str(answer))
                
        except:
            self.screen.setText("ERROR")
            
    #Square root functionality
    #Waits for a number to be pressed first before it functions
    #Only works for the current number not expressions within ()
    def sqroot(self):
        current_txt = self.screen.text()
        nums = self.split_up(current_txt)
        
        try:
            num = float(nums[-1])
            answer = pow(num,0.5)
            
            try:   
                if current_txt[-len(nums[-1])-1] == '-':
                    if len(nums) == 1 or current_txt[-len(nums[-1])-2].isdigit() is False:
                        current_txt = "ERROR"
                    else:
                        current_txt = current_txt[:-len(nums[-1])]+ str(answer)
                        
                elif current_txt[-len(nums[-1])-1] in '*/+':
                    current_txt = current_txt[:-len(nums[-1])]+ str(answer)
                    
            except IndexError:
                current_txt = current_txt[:-len(nums[-1])]+ str(answer)  
                    
            self.screen.setText(current_txt)
            
        except:
             self.screen.setText("ERROR")
             
    #Square functionality
    #Waits for a number to be pressed first before it functions
    #Only works for the current number not expressions
    def squared(self):
        current_txt = self.screen.text()
        nums = self.split_up(current_txt)
        index = 0
    
        try:
            if nums[-1].isdecimal(): 
                num = int(nums[-1])
                
            else : num = float(nums[-1])
            
            answer = pow(num,2)
            
            if current_txt[-1] == ')':
                self.screen.setText(current_txt)
                
            else:    
                if '-' in current_txt and current_txt[-len(nums[-1])-1] == '-':
                    if len(nums) > 1 and current_txt[-len(nums[-1])-2].isdigit():
                        index = -len(nums[-1])
                    else:
                        index = -len(nums[-1])-1
                    
                else:  
                    index = -len(nums[-1])
            
                current_txt = current_txt[:index]+ str(answer)   
                self.screen.setText(current_txt)
                
        except:
            self.screen.setText("ERROR")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = WindowSetup(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
