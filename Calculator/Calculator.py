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
        self.horizontal_ayout_6 = QtWidgets.QHBoxLayout()
        
        window.setCentralWidget(self.central_widget)
    
import Assets

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = WindowSetup(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
