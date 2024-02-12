from PyQt5 import QtCore, QtGui, QtWidgets
from List_ui_structure import Page
from Menu_bar import Menu
import Assets


class New_Button():
    def __init__(self,icon,font):
        self.window = QtWidgets.QMainWindow()
        self.window.setWindowTitle("New list")
        self.window.setFixedSize(300,100)
        self.window.setWindowIcon(icon)
        
        self.centralwidget = QtWidgets.QWidget(self.window)
        self.grid_layout = QtWidgets.QGridLayout(self.centralwidget)
        
        self.name_box = QtWidgets.QLineEdit(self.window)
        self.name_box.setFont(font)
        self.name_box.setPlaceholderText("Rename list")
        self.grid_layout.addWidget(self.name_box, 0, 0, 0, 0)
        
        self.save = QtWidgets.QPushButton("Save")
        self.save.setFont(font)
        self.save.setMaximumWidth(50)
        self.grid_layout.addWidget(self.save, 1, 1, 1, 1)
        
        self.window.setCentralWidget(self.centralwidget)
        
class Signal(QtCore.QObject):
    signal = QtCore.pyqtSignal(str)
        
class Main_Window():
    def __init__(self, window):
        super().__init__()
        #window setup
        window.setWindowTitle("TaskMaster To-Do")
        window.resize(880, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icons/Icons/To-do.png"))
        window.setWindowIcon(icon)
        
        #layout settings
        self.centralwidget = QtWidgets.QWidget(window)
        self.grid_layout = QtWidgets.QGridLayout(self.centralwidget)
        
        #General font 
        self.font = QtGui.QFont()
        self.font.setPointSize(10)
        self.title_font = QtGui.QFont()
        self.title_font.setFamily("Yu Gothic UI Light")
        
        self.emit_ = Signal()
        self.emit_.signal.connect(self.create_new_list)
        
        self.new_list_window = New_Button(icon,self.font)
        self.new_list_window.save.clicked.connect(self.fetch_new_list_name)
        
        #Menu bar
        self.menu = Menu(self.font,window)
        self.menu_bar = self.menu.menu_bar
        self.menu.add_list_button.clicked.connect(self.new_list)
        
        self.grid_layout.addWidget(self.menu_bar, 0, 0, 1, 1)
        
        self.MainWindow = QtWidgets.QStackedWidget(self.centralwidget)
        
        #Today's to do list setup
        self.today = Page(self.font,self.title_font)
        self.today_list = self.today.page
        self.today_list_title = self.today.list_title
        self.today_list_title.setText("<html><head/><body><p><span style=\"\
                            font-size:14pt; font-weight:600;\">Today</span></p></body></html>")
        self.MainWindow.addWidget(self.today_list)
        
        #Important items list setup
        self.important_ = Page(self.font,self.title_font)
        self.important_list = self.important_.page
        self.important_list_title = self.important_.list_title
        self.important_list_title.setText("<html><head/><body><p><span style=\" \
                        font-size:14pt; font-weight:600;\">Important</span></p></body></html>")
        self.MainWindow.addWidget(self.important_list)
        
        #All planned items list setup
        self.all = Page(self.font,self.title_font)
        self.all_list = self.all.page
        self.all_list_title = self.all.list_title
        self.all_list_title.setText("<html><head/><body><p><span style=\"\
                            font-size:14pt; font-weight:600;\">All</span></p></body></html>")
        self.MainWindow.addWidget(self.all_list)
        
        #Completed items list setup
        self.completed = QtWidgets.QWidget()
        self.grid_layout_2 = QtWidgets.QGridLayout(self.completed)
        
        self.completed_list_title = QtWidgets.QLabel(self.completed)
        self.completed_list_title.setFont(self.title_font)
        self.completed_list_title.setText("<html><head/><body><p><span style=\"\
                    font-size:14pt; font-weight:600;\">Mastered</span></p></body></html>")
        self.grid_layout_2.addWidget(self.completed_list_title, 0, 0, 1, 1)
        
        spacer2 = QtWidgets.QSpacerItem(169, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.grid_layout_2.addItem(spacer2, 0, 1, 1, 1)
        
        self.clear_list_button_4 = QtWidgets.QPushButton(self.completed)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icons/Icons/bin.png"))
        self.clear_list_button_4.setIcon(icon)
        self.clear_list_button_4.setFlat(True)
        self.grid_layout_2.addWidget(self.clear_list_button_4, 0, 2, 1, 1)
        
        self.complete_list = QtWidgets.QListWidget(self.completed)
        self.complete_list.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.grid_layout_2.addWidget(self.complete_list, 1, 0, 1, 3)
        
        self.line = QtWidgets.QFrame(self.completed)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.grid_layout_2.addWidget(self.line, 2, 0, 1, 3)
        
        #Updating window layout settings
        self.MainWindow.addWidget(self.completed)
        self.grid_layout.addWidget(self.MainWindow, 0, 1, 1, 1)
        window.setCentralWidget(self.centralwidget)
        
        self.MainWindow.setCurrentIndex(0)
        self.menu.today_button.setChecked(True)
        QtCore.QMetaObject.connectSlotsByName(window)
        
    def fetch_new_list_name(self):
        self.emit_.signal.emit(self.new_list_window.name_box.text())
        self.new_list_window.window.close()
        self.new_list_window.name_box.setText("")
        
    def create_new_list(self,txt):
        new_button = QtWidgets.QPushButton(self.menu.menu_bar)
        new_button.setText(txt)
        new_button.setFont(self.font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icons/Icons/list.png"))
        new_button.setIcon(icon)
        new_button.setCheckable(True)
        new_button.setAutoExclusive(True)
        new_button.setFlat(True)
        self.menu.buttons_list.append(new_button.text())
        self.menu.vertical_layout.addWidget(new_button)
         
    def new_list(self):
        print(self.menu.buttons_list)
        self.new_list_window.window.show()
        
    # def selected():
            
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    ui = Main_Window(window)
    window.show()
    sys.exit(app.exec_())
