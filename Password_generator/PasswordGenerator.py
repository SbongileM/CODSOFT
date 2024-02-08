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
from PyQt5 import QtGui, QtWidgets
import Assets

#The following class sets up the application window and executes the fuctionality of the
#application
class UI_setup():
    def __init__(self,window):
        super().__init__()
        
        #window settings
        window.setWindowTitle("PasswordGenerator")
        window.resize(600,145)
        window.setMaximumSize(700,150)
        window.setWindowIcon(QtGui.QIcon(':/Icons/PasswordIcon.png'))
        
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PasswordGenerator = QtWidgets.QMainWindow()
    ui = UI_setup(PasswordGenerator)
    PasswordGenerator.show()
    sys.exit(app.exec_())