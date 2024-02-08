'''
Author: Sbongile Mdaki
Date:  22 January 2023
Project: GUI desktop password generator application for CodSoft internship

This project aims to create a password generator application using Python.It prompts the user 
to specify the desired length of the password and the complexity.Uses a combination of random 
characters to generate a password of the specified length. Then prints the generated password 
on the screen.The user has the freedom to select the type of characters they want to include
in the password.
'''
from random import randint as randm
from PyQt5 import QtGui, QtWidgets
import Assets

#The following class sets up the application window and executes the fuctionality of the
#application
class UISetup():
    def __init__(self,window):
        super().__init__()
        #Private variables for character/complexity options
        self._characters = []
        self._alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self._nums =  "0123456789"
        self._chars = "'"+'!"#$%&()*+,-./:;<=>?@[]^_`{|}~'
        
        #window settings
        window.setWindowTitle("PasswordGenerator")
        window.resize(600,145)
        window.setMaximumSize(700,150)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icons/PasswordIcon.png"))
        window.setWindowIcon(icon)
        
        #window layout settings
        self.centralwidget = QtWidgets.QWidget(window)
        self.vertical_layout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.horizontal_layout = QtWidgets.QHBoxLayout()
        self.horizontal_layout_2 = QtWidgets.QHBoxLayout()
        self.spacer = QtWidgets.QSpacerItem(40, 20)
        
        #Font settings
        self.font = QtGui.QFont()
        self.font.setPointSize(12)
        self.font.setBold(True)
        self.font.setWeight(75)
        
        #Prompt label settings
        self.prompt = QtWidgets.QLabel("Specify the desired password length :")
        self.prompt.setFont(self.font)
        self.horizontal_layout.addWidget(self.prompt)
        
        #Input or entry widget setup
        self.line_edit = QtWidgets.QLineEdit("")
        self.line_edit.setFont(self.font)
        self.line_edit.setFrame(False)
        self.line_edit.setStyleSheet("background-color:rgb(240,240,230);")
        self.horizontal_layout.addWidget(self.line_edit)
        
        self.vertical_layout.addLayout(self.horizontal_layout)
        
        #Complexity or character options selection radio buttons
        self.ABC = QtWidgets.QRadioButton("ABCD", toggled = lambda:
                                        self.selected(self._alphabets,self.ABC))
        self.ABC.setFont(self.font)
        self.ABC.setAutoExclusive(False)
        self.horizontal_layout_2.addWidget(self.ABC)
        self.horizontal_layout_2.addItem(self.spacer)
        
        self.abc = QtWidgets.QRadioButton("abcd", toggled = lambda:
                                        self.selected(self._alphabets.lower(),self.abc))
        self.abc.setFont(self.font)
        self.abc.setAutoExclusive(False)
        self.horizontal_layout_2.addWidget(self.abc)
        self.horizontal_layout_2.addItem(self.spacer)

        self.numbers = QtWidgets.QRadioButton("1234", toggled = lambda:
                                            self.selected(self._nums, self.numbers))
        self.numbers.setFont(self.font)
        self.numbers.setAutoExclusive(False)
        self.horizontal_layout_2.addWidget(self.numbers)
        self.horizontal_layout_2.addItem(self.spacer)

        self.special_chars = QtWidgets.QRadioButton("@#$*", toggled = lambda:
                                                self.selected(self._chars,self.special_chars))
        self.special_chars.setFont(self.font)
        self.special_chars.setAutoExclusive(False)
        self.horizontal_layout_2.addWidget(self.special_chars)
        self.horizontal_layout_2.addItem(self.spacer)
        
        #Enter button settings
        self.enter_button = QtWidgets.QPushButton("Enter", clicked = lambda:
                                                self.generate_password())
        self.enter_button.setFixedSize(75,27)
        self.enter_button.setFont(self.font)
        self.horizontal_layout_2.addWidget(self.enter_button)
        
        self.vertical_layout.addLayout(self.horizontal_layout_2)
        
        #Output label settings
        self.output = QtWidgets.QLineEdit("")
        self.output.setFont(self.font)
        self.output.setFrame(False)
        self.output.setReadOnly(True)
        self.output.setStyleSheet("background-color:rgb(240,240,230);")
        self.vertical_layout.addWidget(self.output)
        
        window.setCentralWidget(self.centralwidget)       
        
    #This function generates a password containing the selected characters and the 
    #given length, and then displays it on the screen. The returned password can be copied
    def generate_password(self):     
        length = self.line_edit.text()
        password = ""
                       
        try:
            length = int(length)
        except ValueError:
            self.output.setText('Specified length must be a whole number')
        else:
            if length not in range(8,51):
                self.output.setText("Specified length must be between 8 and 50 characters")
                    
            #If none of the options are selected, the application prompts the user to
            #select one before the application continues to run
            elif self.ABC.isChecked()==self.abc.isChecked()==self.numbers.isChecked()==\
                    self.special_chars.isChecked()==False:
                self.output.setText("You have to select at least one option")
                
            #Prints a random password of the specified length
            else:
                characters = "".join(self._characters)
                    
                for i in range(length):
                    password = password + characters[randm(0,len(characters)-1)]
                self.output.setText(f'Password is : {password}')
                
    #Slot(function) gets executed when any of the radio buttons is selected or 
    #unselected (toggled)
    def selected(self,chars, option):
        if option.isChecked() and chars not in self._characters:
            self._characters.append(chars)
        else:
            self._characters.remove(chars)  
                        
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    passwordGenerator = QtWidgets.QMainWindow()
    ui = UISetup(passwordGenerator)
    passwordGenerator.show()
    sys.exit(app.exec_())
    