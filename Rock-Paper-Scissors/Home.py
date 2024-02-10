from PyQt5 import QtCore, QtWidgets

class Home():
    def __init__(self,button_font):
        super().__init__()
        #Home page
        self.home = QtWidgets.QWidget()
        
        #Game rules
        self.home_screen = QtWidgets.QLabel(self.home)
        self.home_screen.setText("<html><head/><body><p><img src=\":/Icons/Help.png\"/></p></body></html>")       
        self.home_screen.setGeometry(QtCore.QRect(0, -10, 571, 500))

        #Play button settings
        self.play_button = QtWidgets.QPushButton(self.home)
        self.play_button.setText("Play")
        self.play_button.setFont(button_font)
        self.play_button.setGeometry(QtCore.QRect(410, 470, 75, 23))
        self.play_button.setStyleSheet("color: rgb(85, 170, 0);")
        
        #Home quit button settings
        self.quit_button = QtWidgets.QPushButton(self.home)
        self.quit_button.setText("Quit")
        self.quit_button.setFont(button_font)
        self.quit_button.setStyleSheet("color: rgb(213, 0, 106);")
        self.quit_button.setGeometry(QtCore.QRect(500, 470, 75, 23))