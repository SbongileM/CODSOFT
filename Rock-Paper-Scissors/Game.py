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
from random import randint as draw
from PyQt5 import QtCore, QtGui, QtWidgets
import Resources
from Home import Home
from Loading import loading
from GameOver import gameOver

#Emits a signal when the player move has been selected
class Player_Signal(QtCore.QObject):
    emit_signal = QtCore.pyqtSignal(str)


#Game window class
class Game():
    def __init__(self,window):
        super().__init__()
        
        #String values that copy both player and computer moves
        self.player_move = ""
        self.computer_move = ""
        
        #Player signal
        self.player_signal = Player_Signal()
        #copying emitted player move into the set_player_move function
        self.player_signal.emit_signal.connect(self.set_player_move)
        
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
        
        #Fighter selection page
        self.selection = QtWidgets.QWidget()
        #Rock selection button
        self.rock = QtWidgets.QPushButton(self.selection,clicked = lambda: self.selected("rock"))
        self.rock.setGeometry(QtCore.QRect(10, 10, 181, 181))
        self.rock.setStyleSheet("image: url(:/Icons/rock_left.png);")
        self.rock.setFlat(True)
        #Paper selection button
        self.paper = QtWidgets.QPushButton(self.selection,clicked = lambda: self.selected("paper"))
        self.paper.setGeometry(QtCore.QRect(370, 10, 181, 181))
        self.paper.setStyleSheet("image: url(:/Icons/paper_left.png);")
        self.paper.setFlat(True)
        #Scissors selection button
        self.scissors = QtWidgets.QPushButton(self.selection,clicked = lambda: self.selected("scissors"))
        self.scissors.setGeometry(QtCore.QRect(200, 280, 181, 181))
        self.scissors.setStyleSheet("image: url(:/Icons/scissors_left.png);")
        self.scissors.setFlat(True)
        #Selection instruction label
        self.select = QtWidgets.QLabel(self.selection)
        self.select.setFont(font)
        self.select.setText("<html><head/><body><p><span style=\" font-size:24pt; font-weight:600; color:#55aa00;\"\
                            >Pick your fighter</span></p></body></html>")
        self.select.setGeometry(QtCore.QRect(140, 210, 291, 41))
        #Selection page quit button
        self.quit_button = QtWidgets.QPushButton(self.selection)
        #connecting quit push button to Qt window close functionality
        self.quit_button.clicked.connect(window.close)
        self.quit_button.setText("Quit")
        self.quit_button.setGeometry(QtCore.QRect(500, 470, 75, 23))
        self.quit_button.setFont(button_font)
        self.quit_button.setStyleSheet("color: rgb(213, 0, 106);")
        self.stacked_widget.addWidget(self.selection)
        
        #Loading page
        self.loading = loading(font)
        #First Loading page
        self.loading1 = self.loading.Loading1
        self.stacked_widget.addWidget(self.loading1)
        #Second Loading Page
        self.loading2 = self.loading.Loading2
        self.stacked_widget.addWidget(self.loading2)
        
        #Game over page
        self.game_over = gameOver(font,button_font)
        self.game_over_page = self.game_over.game_over
        #connecting quit push button to Qt window close functionality
        self.game_over.quit_button.clicked.connect(window.close)
        #connecting replay push button to replay the game
        self.game_over.replay_button.clicked.connect(self.replay)
        self.stacked_widget.addWidget(self.game_over_page)
        
        #Setting first window to home page
        self.stacked_widget.setCurrentIndex(0)
        
        self.vertical_layout.addWidget(self.stacked_widget)
        window.setCentralWidget(self.centralwidget)
        QtCore.QMetaObject.connectSlotsByName(window)
     
    #Game window functions
    #Commences game when player clicks the Play push button 
    def start(self):
        #sets window to display move selection page
        self.stacked_widget.setCurrentIndex(1)
        
    #Commences another game round when player clicks the Replay push button 
    def replay(self):
        #sets window to display move selection page
        self.stacked_widget.setCurrentIndex(1)
        
    #Sets player move when it has been selected
    def set_player_move(self,move):
        self.player_move = move
        
    #Generates random move for the computer
    def draw_computer_fighter(self):
        options = ["rock","paper","scissors"]
        return options[draw(0,2)]
        
    #Creates a time delay of 0.8 seconds for switching pages
    def delay(self):
        self.timer = QtCore.QTimer()
        self.timer.start(800)
        self.timer.timeout.connect(self.switch_pages)
    
    #Works together with the delay function to swap game pages    
    def switch_pages(self):
        index = self.stacked_widget.currentIndex()

        if index == 2:
            self.stacked_widget.setCurrentIndex(3)
        elif index == 3:
            self.stacked_widget.setCurrentIndex(4)
        else:
            self.stacked_widget.setCurrentIndex(index)
        
    #Basically the game loop. It checkes the move the player has selected, 
    #emits the signal, and then set the game over results.
    def selected(self,pressed):
        if pressed == "rock" or pressed == "paper" or pressed == "scissors":
            #emits signal once player has selected their move
            self.player_signal.emit_signal.emit(pressed)
            #sets current page to Loading page
            self.stacked_widget.setCurrentIndex(2)
            #Swaps pages until the game over page is reached
            self.delay()
    
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    game_window = QtWidgets.QMainWindow()
    ui = Game(game_window)
    game_window.show()
    sys.exit(app.exec_())