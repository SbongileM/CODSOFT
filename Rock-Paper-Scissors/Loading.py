from PyQt5 import QtCore, QtWidgets

class loading():
    def __init__(self,font):
        super().__init__()

        #First Loading page
        self.Loading1 = QtWidgets.QWidget()
        
        #Player label
        self.player = QtWidgets.QLabel(self.Loading1)
        self.player.setText("<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#55aa00;\"\
                            >Player</span></p></body></html>")
        self.player.setFont(font)
        self.player.setGeometry(QtCore.QRect(80, 460, 81, 41))
        
        #Player icon
        self.player_icon = QtWidgets.QPushButton(self.Loading1)
        self.player_icon.setEnabled(False)
        self.player_icon.setGeometry(QtCore.QRect(330, 0, 240, 240))
        self.player_icon.setStyleSheet("image: url(:/Icons/rock_right.png);")
        self.player_icon.setCheckable(False)
        self.player_icon.setFlat(True)
        
        #Computer label
        self.computer = QtWidgets.QLabel(self.Loading1)
        self.computer.setFont(font)
        self.computer.setText("<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#55aa00;\"\
                               >Computer</span></p></body></html>")
        self.computer.setGeometry(QtCore.QRect(410, 230, 101, 41))
        
        #Computer icon
        self.computer_icon = QtWidgets.QPushButton(self.Loading1)
        self.computer_icon.setEnabled(False)
        self.computer_icon.setGeometry(QtCore.QRect(0, 220, 240, 240))
        self.computer_icon.setStyleSheet("image: url(:/Icons/rock_left.png);")
        self.computer_icon.setCheckable(False)
        self.computer_icon.setFlat(True)
        
        #Rock
        self.state = QtWidgets.QLabel(self.Loading1)
        self.state.setText("<html><head/><body><p><span style=\" font-size:24pt; font-weight:600; color:#55aa00;\"\
                             >ROCK</span></p></body></html>")
        self.state.setFont(font)
        self.state.setGeometry(QtCore.QRect(220, 190, 121, 41))
        
        #Second Loading Page
        self.Loading2 = QtWidgets.QWidget()

        #Player label
        self.player = QtWidgets.QLabel(self.Loading2)
        self.player.setFont(font)
        self.player.setText("<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#55aa00;\"\
                            >Player</span></p></body></html>")
        self.player.setGeometry(QtCore.QRect(420, 460, 81, 41))
        
        #Player icon
        self.player_icon = QtWidgets.QPushButton(self.Loading2)
        self.player_icon.setEnabled(False)
        self.player_icon.setGeometry(QtCore.QRect(320, 230, 240, 240))
        self.player_icon.setStyleSheet("image: url(:/Icons/rock_right.png);")
        self.player_icon.setCheckable(False)
        self.player_icon.setFlat(True)
        
        #Computer label
        self.computer = QtWidgets.QLabel(self.Loading2)
        self.computer.setFont(font)
        self.computer.setText("<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#55aa00;\"\
                               >Computer</span></p></body></html>")
        self.computer.setGeometry(QtCore.QRect(70, 230, 101, 41))
        
        #Computer icon
        self.computer_icon = QtWidgets.QPushButton(self.Loading2)
        self.computer_icon.setEnabled(False)
        self.computer_icon.setGeometry(QtCore.QRect(0, 0, 240, 240))
        self.computer_icon.setStyleSheet("image: url(:/Icons/rock_left.png);")
        self.computer_icon.setCheckable(False)
        self.computer_icon.setFlat(True)
        
        #Paper
        self.state = QtWidgets.QLabel(self.Loading2)
        self.state.setFont(font)
        self.state.setText("<html><head/><body><p><span style=\" font-size:24pt; font-weight:600; color:#55aa00;\"\
                             >PAPER</span></p></body></html>")
        self.state.setGeometry(QtCore.QRect(240, 200, 121, 41))
