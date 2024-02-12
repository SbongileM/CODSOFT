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
        
        #Signal for creation of a new list
        self.emit_ = Signal()
        self.emit_.signal.connect(self.create_new_list)
        
        self.new_list_window = New_Button(icon,self.font)
        self.new_list_window.save.clicked.connect(self.fetch_new_list_name)
        
        #Menu bar
        self.menu = Menu(self.font,window)
        self.menu_bar = self.menu.menu_bar
        self.menu.add_list_button.clicked.connect(self.new_list)
        self.grid_layout.addWidget(self.menu_bar, 0, 0, 1, 1)
        #Stacked widget for list pages
        self.MainWindow = QtWidgets.QStackedWidget(self.centralwidget)
        #Create list pages
        self.create_pages()
        self.grid_layout.addWidget(self.MainWindow, 0, 1, 1, 1)
        window.setCentralWidget(self.centralwidget)
        #Connect all current buttons to the selected function
        self.connect_slots()
        #Set initial page to today's list
        self.MainWindow.setCurrentIndex(0)
        self.menu.today_button.setChecked(True)
        QtCore.QMetaObject.connectSlotsByName(window)
        
    #Emits signal containing the name of a new list that has been created
    def fetch_new_list_name(self):
        self.emit_.signal.emit(self.new_list_window.name_box.text())
        self.new_list_window.window.close()
        self.new_list_window.name_box.setText("")
        
    #Creates a new list button and page
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
        self.menu.buttons_list.append(new_button)
        self.create_page(txt)
        self.menu.vertical_layout.addWidget(new_button)
        #Update signals accepted by the selected function
        self.connect_slots()
         
    #Shows the new list name edit window when new_list button is selected
    def new_list(self):
        self.new_list_window.window.show()
        
    #Creates a list page
    def create_page(self,name):
        list_ = Page(self.font,self.title_font)
        title = list_.list_title
        title.setText(f"<html><head/><body><p><span style=\"\
                    font-size:14pt; font-weight:600;\">{name}</span></p></body></html>")
        self.MainWindow.addWidget(list_.page)
        
    #Creates all pages currently saved into the data base
    def create_pages(self):
        for button in self.menu.buttons_list:
            self.create_page(button.text())
     
    #Slot for connecting button clicked signal to display corresponding list
    def selected(self):
        index = self.menu.vertical_layout.indexOf(self.centralwidget.sender())
        self.menu.buttons_list[index].setChecked(True)
        self.MainWindow.setCurrentIndex(index)
        
    #Connect all the menu buttons to selected function
    def connect_slots(self):
        for i in range(len(self.menu.buttons_list)):
            self.menu.buttons_list[i].clicked.connect(lambda: self.selected())
                                  
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    ui = Main_Window(window)
    window.show()
    sys.exit(app.exec_())
