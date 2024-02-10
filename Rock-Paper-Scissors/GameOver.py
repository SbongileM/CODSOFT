from PyQt5 import QtCore, QtWidgets

class gameOver():
    def __init__(self,font,button_font):
        super().__init__()
        #Game over page
        self.game_over = QtWidgets.QWidget()
        
        #Scoreboard layout settings
        self.vertical_layout = QtWidgets.QWidget(self.game_over)
        self.vertical_layout.setGeometry(QtCore.QRect(10, 0, 161, 101))
        self.scoreBoard = QtWidgets.QVBoxLayout(self.vertical_layout)
        
        #Scoreboard title
        self.score_title = QtWidgets.QLabel(self.vertical_layout)
        self.score_title.setFont(font)
        self.score_title.setText("<html><head/><body><p><span style=\" \
                                  font-size:14pt; font-weight:600; text-decoration: underline; color:#55aa00;\"\
                                  >Score Board</span></p></body></html>")
        self.scoreBoard.addWidget(self.score_title)
        
        #Computer score label
        self.computer_score = QtWidgets.QLabel(self.vertical_layout)
        self.computer_score.setFont(font)
        self.scoreBoard.addWidget(self.computer_score)
        
        #Player score label
        self.player_score = QtWidgets.QLabel(self.vertical_layout)
        self.player_score.setFont(font)
        self.scoreBoard.addWidget(self.player_score)
        
        #Computer label
        self.computer = QtWidgets.QLabel(self.game_over)
        self.computer.setGeometry(QtCore.QRect(410, 230, 101, 41))
        self.computer.setFont(font)
        self.computer.setText("<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#55aa00;\"\
                               >Computer</span></p></body></html>")
        
        #Computer icon
        self.computer_icon = QtWidgets.QPushButton(self.game_over)
        self.computer_icon.setEnabled(False)
        self.computer_icon.setGeometry(QtCore.QRect(330, 0, 240, 240))
        self.computer_icon.setCheckable(False)
        self.computer_icon.setFlat(True)
        
        #Player label
        self.player = QtWidgets.QLabel(self.game_over)
        self.player.setFont(font)
        self.player.setGeometry(QtCore.QRect(80, 460, 81, 41))
        self.player.setText("<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#55aa00;\"\
                            >Player</span></p></body></html>")

        #Player icon
        self.player_icon = QtWidgets.QPushButton(self.game_over)
        self.player_icon.setEnabled(False)
        self.player_icon.setGeometry(QtCore.QRect(0, 220, 240, 240))
        self.player_icon.setCheckable(False)
        self.player_icon.setFlat(True)
        
        #Scissors game state
        self.state = QtWidgets.QLabel(self.game_over)
        self.state.setGeometry(QtCore.QRect(180, 190, 161, 41))
        self.state.setFont(font)
        self.state.setText("<html><head/><body><p><span style=\" font-size:24pt; font-weight:600; color:#55aa00;\"\
                             >SCISSORS</span></p></body></html>")
        
        #Outcome
        self.outcome = QtWidgets.QLabel(self.game_over)
        self.outcome.setGeometry(QtCore.QRect(330, 340, 200, 41))
        self.outcome.setFont(font)
        
        #Replay button settings
        self.replay_button = QtWidgets.QPushButton(self.game_over)
        self.replay_button.setText("Replay")
        self.replay_button.setGeometry(QtCore.QRect(410, 470, 75, 23))
        self.replay_button.setFont(button_font)
        self.replay_button.setStyleSheet("color: rgb(85, 170, 0);")
        
        #Quit button
        self.quit_button = QtWidgets.QPushButton(self.game_over)
        self.quit_button.setText("Quit")
        self.quit_button.setGeometry(QtCore.QRect(500, 470, 75, 23))
        self.quit_button.setFont(button_font)
        self.quit_button.setStyleSheet("color: rgb(213, 0, 106);")