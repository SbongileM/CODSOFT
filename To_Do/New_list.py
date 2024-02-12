from PyQt5 import QtCore, QtGui, QtWidgets

class New_Button():
    def __init__(self,icon,font):
        #Window setup
        self.window = QtWidgets.QMainWindow()
        self.window.setWindowTitle("New list")
        self.window.setFixedSize(300,100)
        self.window.setWindowIcon(icon)
        
        #Layout settings
        self.centralwidget = QtWidgets.QWidget(self.window)
        self.grid_layout = QtWidgets.QGridLayout(self.centralwidget)
        
        #New list name edit input box
        self.name_box = QtWidgets.QLineEdit(self.window)
        self.name_box.setFont(font)
        self.name_box.setPlaceholderText("Rename list")
        self.grid_layout.addWidget(self.name_box, 0, 0, 0, 0)
        
        #Save button
        self.save = QtWidgets.QPushButton("Save")
        self.save.setFont(font)
        self.save.setMaximumWidth(50)
        self.grid_layout.addWidget(self.save, 1, 1, 1, 1)
        
        self.window.setCentralWidget(self.centralwidget)  