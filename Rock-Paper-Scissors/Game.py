'''
Author: Sbongile Mdaki
Date:  28 January 2023
Project: GUI desktop Rock-Paper-Scissors application for CodSoft internship

This project aims to create a user-friendly interface with clear instructions and
feedback with the following functionalities:
1.Prompts the user to choose rock, paper, or scissors.
2.Generates a random choice (rock, paper, or scissors) for the computer.
3.Determines the winner based on the user's choice and the
computer's choice, using the game rules displayed on the home window.Rock beats 
scissors, scissors beat paper, and paper beats rock.
4.Displays the user's choice and the computer's choice, and the result, whether 
the user wins, loses, or it's a tie.
5. Score tracking to keep track of the user's and computer's scores for
multiple rounds.
6.Replay for the user if they want to play another round.

'''

from PyQt5 import QtCore, QtGui, QtWidgets
import Resources
from Home import Home


#Game window class
class Game():
    def __init__(self,window):
        super().__init__()
        
        #Main window settings
        window.setWindowTitle("Rock-Paper-Scissors")
        window.resize(598, 630)
        window.setMinimumSize(QtCore.QSize(600, 630))
        window.setMaximumSize(QtCore.QSize(600, 630))
        
        #Main window icon settings
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icons/Logo.png"))
        window.setWindowIcon(icon)
        
        #Layout settings
        self.centralwidget = QtWidgets.QWidget(window)
        self.vertical_layout = QtWidgets.QVBoxLayout(self.centralwidget)
        
        #General font settings
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        
        #Game title settings
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setFont(font)
        self.title.setText("<html><head/><body><p><span style=\" font-size:45pt; font-weight:600; color:#d9245e;\"\
                           >Rock</span><span style=\" font-size:45pt; font-weight:600; color:#55aa00;\"\
                           >-</span><span style=\" font-size:45pt; font-weight:600; color:#d1d100;\"\
                           >Paper</span><span style=\" font-size:45pt; font-weight:600; color:#55aa00;\"\
                           >-</span><span style=\" font-size:45pt; font-weight:600; color:#55aaff;\"\
                           >Scissors</span></p></body></html>")
        self.vertical_layout.addWidget(self.title)
        
        #Buttons font settings
        button_font = QtGui.QFont()
        button_font.setBold(True)
        button_font.setWeight(75)
        
        #A stacked widget for pages to display game windows
        self.stacked_widget = QtWidgets.QStackedWidget(self.centralwidget)
        
        #Home page
        self.home = Home(button_font)
        self.home_page = self.home.home
        #connecting quit push button to Qt window close functionality
        self.home.quit_button.clicked.connect(window.close)
        #connecting play push button to the game start function
        self.home.play_button.clicked.connect(self.start)
        self.stacked_widget.addWidget(self.home_page)
        
        #Setting first window to home page
        self.stacked_widget.setCurrentIndex(0)
        
        self.vertical_layout.addWidget(self.stacked_widget)
        window.setCentralWidget(self.centralwidget)
        QtCore.QMetaObject.connectSlotsByName(window)
     
    #Game window functionalities
    
    #Commences game when player clicks the Play push button 
    def start(self):
        pass
    
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    game_window = QtWidgets.QMainWindow()
    ui = Game(game_window)
    game_window.show()
    sys.exit(app.exec_())