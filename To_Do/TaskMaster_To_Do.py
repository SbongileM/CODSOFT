from PyQt5 import QtCore, QtGui, QtWidgets
from List_ui_structure import Page
from Menu_bar import Menu
from Task_window import Task_Window
from New_list import New_Button
import Assets

#Emits a signal when a new list is created
class NewListSignal(QtCore.QObject):
    signal = QtCore.pyqtSignal(str)
    
#Emits signal when task item is selected
class List_Signal(QtWidgets.QListWidget):
    signal = QtCore.pyqtSignal(str)
    
    def mousePressEvent(self,event):
        task = self.itemAt(event.pos())
        if task:
            self.signal.emit(task.text())
        super().mousePressEvent(event)
  
class Main_Window():
    def __init__(self, window):
        super().__init__()
        #Container for all the currently available lists
        self.lists = []
        #window setup
        window.setWindowTitle("TaskMaster To-Do")
        window.resize(880, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icons/Icons/To-do.png"))
        window.setWindowIcon(icon)
        
        #layout settings
        self.centralwidget = QtWidgets.QWidget(window)
        self.grid_layout = QtWidgets.QGridLayout(self.centralwidget)
        
        #General font settings
        self.font = QtGui.QFont()
        self.font.setPointSize(10)
        self.title_font = QtGui.QFont()
        self.title_font.setFamily("Yu Gothic UI Light")
        
        #Signal for creation of a new list
        self.emit_ = NewListSignal()
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
        self.connect_list_buttons()
        
        #Set initial page to today's list
        self.MainWindow.setCurrentIndex(0)
        self.menu.today_button.setChecked(True)
        QtCore.QMetaObject.connectSlotsByName(window)
        
    #Shows the new list name edit window when new_list button is selected
    def new_list(self):
        self.new_list_window.window.show()
        
    #Creates all pages currently saved into the data base
    def create_pages(self):
        for button in self.menu.buttons_list:
            self.create_page(button.text())
            
    #Slot for connecting button clicked signal to display corresponding list
    def selected(self):
        index = self.menu.vertical_layout.indexOf(self.centralwidget.sender())
        self.menu.buttons_list[index].setChecked(True)
        self.MainWindow.setCurrentIndex(index)
        
    #Emits signal containing the name of a new list that has been created
    def fetch_new_list_name(self):
        self.emit_.signal.emit(self.new_list_window.name_box.text())
        self.new_list_window.window.close()
        self.new_list_window.name_box.setText("")
        
    #Clears the contents of the current list
    def clear_list(self):
        index = self.MainWindow.currentIndex()
        self.lists[index].task_list.clear()
        
    #Connect all the menu buttons to selected function
    def connect_slots(self):
        for i in range(len(self.menu.buttons_list)):
            self.menu.buttons_list[i].clicked.connect(lambda: self.selected())
        
    #Delete current task    
    def delete_task(self,item,index):
        self.lists[index].task_list.takeItem(item)
        self.task_window.window.close()
        
    #Cancel any changes made to current task
    def cancel_task_edit(self,item):
        self.lists[0].task_list.takeItem(item)
        self.lists[1].task_list.takeItem(item)
        self.task_window.window.close()
        
    #Connect current list buttons to their corresponding signal slots
    def connect_list_buttons(self):
        for i in range(len(self.lists)):
            self.lists[i].add_task_button.clicked.connect(lambda:self.add_item())
            self.lists[i].clear_list_button.clicked.connect(lambda:self.clear_list())
            self.lists[i].task_list.itemClicked.connect(self.open_task_window)
            
    #Add current task to Important list
    def mark_task_as_important(self,item):
        if self.lists[1].task_list.findItems(item, QtCore.Qt.MatchExactly):
            pass
        else:
            self.lists[1].task_list.addItem(item)
        
    #Add current task to Today list
    def add_to_today(self,item):
        if self.lists[0].task_list.findItems(item, QtCore.Qt.MatchExactly):
            pass
        else:
            self.lists[0].task_list.addItem(item)
        
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
        self.connect_list_buttons()
         
    #Creates a list page
    def create_page(self,name):
        list_ = Page(self.font,self.title_font)
        title = list_.list_title
        title.setText(f"<html><head/><body><p><span style=\"\
                    font-size:14pt; font-weight:600;\">{name}</span></p></body></html>")
        self.MainWindow.addWidget(list_.page)
        self.lists.append(list_)
        
    #Adds task item in the current list
    def add_item(self):
        index = self.MainWindow.currentIndex()
        item = self.lists[index].new_task_edit.text()
        if self.lists[index].task_list.findItems(item, QtCore.Qt.MatchExactly):
            pass
        else:
            self.lists[index].task_list.addItem(item)
            self.lists[2].task_list.addItem(item)
            
        self.lists[index].new_task_edit.setText("")
    
    #Opens task editing window
    def open_task_window(self): 
        index = self.MainWindow.currentIndex()
        item = self.lists[index].task_list.currentItem().text()
        item_no = self.lists[index].task_list.currentRow() 
        self.task_window = Task_Window(f"Task#{item_no+1}",self.font)
        self.task_window.important.clicked.connect(lambda:self.mark_task_as_important(item))
        self.task_window.add_today.clicked.connect(lambda:self.add_to_today(item))
        self.task_window.save.clicked.connect(self.task_window.window.close)
        self.task_window.cancel.clicked.connect(lambda:self.cancel_task_edit(item_no))
        self.task_window.delete_task.clicked.connect(lambda:self.delete_task(item_no,index))
        self.task_window.window.show()
        
                             
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    ui = Main_Window(window)
    window.show()
    sys.exit(app.exec_())
