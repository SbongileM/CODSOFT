from PyQt5 import QtGui, QtWidgets,QtCore

class Menu():
    def __init__(self,font, window):
        super().__init__()
        self.buttons_list = []
        
        #layout settings
        self.centralwidget = QtWidgets.QWidget(window)
        self.horizontal_layout = QtWidgets.QHBoxLayout()
        self.horizontal_layout_2 = QtWidgets.QHBoxLayout()
        self.horizontal_layout_2.setSpacing(0)
        self.vertical_layout = QtWidgets.QVBoxLayout()

        #Menu bar setup
        self.menu_bar = QtWidgets.QWidget(self.centralwidget)
        self.menu_bar.setMaximumWidth(250)
        self.grid_layout = QtWidgets.QGridLayout(self.menu_bar)
        
        #Spacer
        spacer = QtWidgets.QSpacerItem(20, 50, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.grid_layout.addItem(spacer, 5, 1, 1, 1)
        
        #Menu bar title settings
        self.title_icon = QtWidgets.QLabel(self.menu_bar)
        self.title_icon.setText("<html><head/><body><p><img src=\":/Icons/Icons/To-do_1.png\"\
                                /></p></body></html>")
        self.title_icon.setMaximumSize(QtCore.QSize(30, 30))
        self.horizontal_layout.addWidget(self.title_icon)
        self.app_title = QtWidgets.QLabel(self.menu_bar)
        self.app_title.setText("<html><head/><body><p><span style=\" font-size:14pt;\"\
                                >TaskMaster To-Do</span></p></body></html>")
        self.app_title.setMaximumSize(QtCore.QSize(250, 16777215))
        self.horizontal_layout.addWidget(self.app_title)
        self.grid_layout.addLayout(self.horizontal_layout, 0, 0, 1, 2)
        
        #Seperator
        self.line = QtWidgets.QFrame(self.menu_bar)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.grid_layout.addWidget(self.line, 1, 0, 1, 3)
       
        #Search box settings
        self.search_box = QtWidgets.QLineEdit(self.menu_bar)
        self.search_box.setFont(font)
        self.search_box.setPlaceholderText("Search...")
        self.horizontal_layout_2.addWidget(self.search_box)
        self.search_button = QtWidgets.QPushButton(self.menu_bar)
        self.search_button.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icons/Icons/search.png"))
        self.search_button.setIcon(icon)
        self.search_button.setFlat(True)
        self.horizontal_layout_2.addWidget(self.search_button)
        self.grid_layout.addLayout(self.horizontal_layout_2, 2, 0, 1, 2)
        
        #Seperator
        self.line = QtWidgets.QFrame(self.menu_bar)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.grid_layout.addWidget(self.line, 3, 0, 1, 3)
        
        #Today list button setup
        self.today_button = QtWidgets.QPushButton(self.menu_bar)
        self.today_button.setText("Today")
        self.today_button.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icons/Icons/today.png"))     
        self.today_button.setIcon(icon)
        self.today_button.setCheckable(True)
        self.today_button.setAutoExclusive(True)
        self.today_button.setFlat(True)
        self.vertical_layout.addWidget(self.today_button)
        self.buttons_list.append(self.today_button)
        
        #Important list button setup
        self.important_button = QtWidgets.QPushButton(self.menu_bar)
        self.important_button.setText("Important")
        self.important_button.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icons/Icons/star.png"))  
        self.important_button.setIcon(icon)
        self.important_button.setCheckable(True)
        self.important_button.setAutoExclusive(True)
        self.important_button.setFlat(True)
        self.vertical_layout.addWidget(self.important_button)
        self.buttons_list.append(self.important_button)
        
        #All list button setup
        self.all_button = QtWidgets.QPushButton(self.menu_bar)
        self.all_button.setText("All")
        self.all_button.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icons/Icons/all.png")) 
        self.all_button.setIcon(icon)
        self.all_button.setCheckable(True)
        self.all_button.setAutoExclusive(True)
        self.all_button.setFlat(True)
        self.vertical_layout.addWidget(self.all_button)
        self.buttons_list.append(self.all_button)
        
        #Comleted tasks list button setup
        self.complete_button = QtWidgets.QPushButton(self.menu_bar)
        self.complete_button.setText("Mastered")
        self.complete_button.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icons/Icons/complete.png")) 
        self.complete_button.setIcon(icon)
        self.complete_button.setCheckable(True)
        self.complete_button.setAutoExclusive(True)
        self.complete_button.setFlat(True)
        self.vertical_layout.addWidget(self.complete_button)
        self.buttons_list.append(self.complete_button)
        
        #Work related list button setup
        self.work_button = QtWidgets.QPushButton(self.menu_bar)
        self.work_button.setText("Work")
        self.work_button.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icons/Icons/work.png")) 
        self.work_button.setIcon(icon)
        self.work_button.setCheckable(True)
        self.work_button.setAutoExclusive(True)
        self.work_button.setFlat(True)
        self.vertical_layout.addWidget(self.work_button)
        self.buttons_list.append(self.work_button)
        
        #Workout list button setup
        self.exercise_button = QtWidgets.QPushButton(self.menu_bar)
        self.exercise_button.setText("Exercise")
        self.exercise_button.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icons/Icons/gym.png")) 
        self.exercise_button.setIcon(icon)
        self.exercise_button.setCheckable(True)
        self.exercise_button.setAutoExclusive(True)
        self.exercise_button.setFlat(True)
        self.vertical_layout.addWidget(self.exercise_button)
        self.buttons_list.append(self.exercise_button)
        
        #Shopping list button setup
        self.shopping_button = QtWidgets.QPushButton(self.menu_bar)
        self.shopping_button.setText("Shopping")
        self.shopping_button.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icons/Icons/shopping.png"))
        self.shopping_button.setIcon(icon)
        self.shopping_button.setCheckable(True)
        self.shopping_button.setAutoExclusive(True)
        self.shopping_button.setFlat(True)
        self.vertical_layout.addWidget(self.shopping_button)
        self.buttons_list.append(self.shopping_button)
        self.grid_layout.addLayout(self.vertical_layout, 4, 0, 1, 2)
        
        #Scroll bar setup
        self.scroll_bar = QtWidgets.QScrollBar(self.menu_bar)
        self.scroll_bar.setMaximumSize(QtCore.QSize(10, 16777215))
        self.scroll_bar.setStyleSheet("")
        self.scroll_bar.setOrientation(QtCore.Qt.Vertical)
        self.grid_layout.addWidget(self.scroll_bar, 4, 2, 2, 1, QtCore.Qt.AlignRight)
        
        #Seperator
        self.line = QtWidgets.QFrame(self.menu_bar)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.grid_layout.addWidget(self.line, 6, 0, 1, 3)
        
        #Add new list button setup
        self.add_list_button = QtWidgets.QPushButton(self.menu_bar)
        self.add_list_button.setText("   New list")
        self.add_list_button.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icons/Icons/add.png"))
        self.add_list_button.setIcon(icon)
        self.add_list_button.setCheckable(True)
        self.add_list_button.setFlat(True)
        self.grid_layout.addWidget(self.add_list_button, 7, 0, 1, 3)

        
