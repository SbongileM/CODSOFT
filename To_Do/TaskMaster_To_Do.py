from PyQt5 import QtCore, QtGui, QtWidgets
from List_ui_structure import Page
from Menu_bar import Menu
from Task_window import Task_Window
from New_list import New_Button
from DatabaseManager import DatabaseManager
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
        #data base for new lists
        self.lists_manager = DatabaseManager()
        
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
        
        #Signal for the creation of a new list
        self.emit_ = NewListSignal()
        self.emit_.signal.connect(self.create_new_list)
        self.new_list_window = New_Button(icon,self.font)
        self.new_list_window.save.clicked.connect(self.fetch_new_list_name)
        
        #Menu bar
        self.menu = Menu(self.font,window)
        self.menu_bar = self.menu.menu_bar
        self.menu.add_list_button.clicked.connect(self.new_list)
        self.grid_layout.addWidget(self.menu_bar, 0, 0, 1, 1)
        
        #Container for the created lists
        self.new_lists = [button.text() for button in self.menu.buttons_list]
        self.lists = []

        #Stacked widget for list pages
        self.MainWindow = QtWidgets.QStackedWidget(self.centralwidget)
        #Create list pages
        self.create_pages()
        self.grid_layout.addWidget(self.MainWindow, 0, 1, 1, 1)
        window.setCentralWidget(self.centralwidget)
        #Fetch items from databases
        self.fetch_user_buttons()

        #Add user buttons to menu bar
        if len(self.new_lists) > 7:
            for item in self.new_lists[7:]:
                self.create_button(item)
                self.create_page(item)
            
        #Connect all current buttons to the selected() function
        self.connect_slots()
        self.connect_list_buttons()
        
        #Set initial page to today's list
        self.MainWindow.setCurrentIndex(0)
        self.menu.today_button.setChecked(True)
        QtCore.QMetaObject.connectSlotsByName(window)
      
    """---------------------------Functions that handle lists-------------------------------"""  
    #Shows the new list name edit window when new_list button is selected
    def new_list(self):
        self.new_list_window.window.show()
        
    #Clears the contents of the current list
    def clear_list(self):
        index = self.MainWindow.currentIndex()
        self.lists[index].task_list.clear()

    #Deletes the current list
    def delete_list(self):
        index = self.MainWindow.currentIndex()
        self.menu.buttons_list[index].deleteLater()
        self.MainWindow.removeWidget(self.lists[index].page)
        del(self.lists[index])
        del(self.new_lists[index])
        #Update database
        self.save_user_buttons()
               
    #Connect all the menu buttons to selected function
    def connect_slots(self):
        for i in range(len(self.menu.buttons_list)):
            self.menu.buttons_list[i].clicked.connect(lambda: self.selected())
            
    #Slot for connecting button clicked signal to display corresponding list
    def selected(self):
        index = self.menu.vertical_layout.indexOf(self.centralwidget.sender())
        try:
            self.menu.buttons_list[index].setChecked(True)
            self.MainWindow.setCurrentIndex(index)
        except IndexError:
            pass
        
    #Emits signal containing the name of a new list that has been created
    def fetch_new_list_name(self):
        self.emit_.signal.emit(self.new_list_window.name_box.text())
        self.new_list_window.window.close()
        self.new_list_window.name_box.setText("")
        
    #Connect current list buttons to their corresponding signal slots
    def connect_list_buttons(self):
        for i in range(len(self.lists)):
            self.lists[i].add_task_button.clicked.connect(lambda:self.add_item())
            self.lists[i].clear_list_button.clicked.connect(lambda:self.clear_list())
            self.lists[i].delete_list_button.clicked.connect(lambda:self.delete_list())
            self.lists[i].task_list.itemClicked.connect(self.open_task_window)
            
    #Creates all pages currently saved into the data base
    def create_pages(self):
        for button in self.menu.buttons_list:
            self.create_page(button.text())
            
    #Creates a list page
    def create_page(self,name):
        list_ = Page(self.font,self.title_font)
        title = list_.list_title
        title.setText(f"<html><head/><body><p><span style=\"\
                    font-size:14pt; font-weight:600;\">{name}</span></p></body></html>")
        self.MainWindow.addWidget(list_.page)
        self.lists.append(list_)
        
    def create_button(self,name):
        new_button = QtWidgets.QPushButton(self.menu.menu_bar)
        new_button.setText(name)
        new_button.setFont(self.font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icons/Icons/list.png"))
        new_button.setIcon(icon)
        new_button.setCheckable(True)
        new_button.setAutoExclusive(True)
        new_button.setFlat(True)
        self.menu.buttons_list.append(new_button)
        self.menu.vertical_layout.addWidget(new_button)
        
    #Creates a new list button and page
    def create_new_list(self,txt):
        self.create_button(txt)
        self.new_lists.append(txt)
        self.create_page(txt)
        #Update signals accepted by the selected() function
        self.connect_slots()
        self.connect_list_buttons()
        #Add to database
        self.save_user_buttons()
              
    """-----------------------Functions that handle list items-------------------------------"""
    #Adds task item in the current list
    def add_item(self):
        index = self.MainWindow.currentIndex()
        item = self.lists[index].new_task_edit.text()
        
        if item == "":
            item = "Untitled task"
             
        if not self.lists[index].task_list.findItems(item, QtCore.Qt.MatchExactly):
            self.lists[index].task_list.addItem(item)
            if index != 2:
                self.lists[2].task_list.addItem(item) 
                   
        self.lists[index].new_task_edit.setText("")
    
    #Add current task to Important list
    def mark_task_as_important(self,item):
        if not self.lists[1].task_list.findItems(item, QtCore.Qt.MatchExactly):
            self.lists[1].task_list.addItem(item)
            
    #Add current task to Today list
    def add_to_today(self,item):
        if not self.lists[0].task_list.findItems(item, QtCore.Qt.MatchExactly):
            self.lists[0].task_list.addItem(item)
              
    #Adds current task to completed and removes it from all other lists
    def mark_as_completed(self,item,item_no,index):
        self.lists[3].task_list.addItem(item)
        #Remove from all other primary lists
        self.lists[0].task_list.takeItem(item_no)
        self.lists[1].task_list.takeItem(item_no)
        self.lists[2].task_list.takeItem(item_no)
        self.lists[index].task_list.takeItem(item_no)
        
    #Save current task edits
    def save_task(self,index):
        try:
            notes = self.task_window.notes_edit.toPlainText()
            new_name = self.task_window.task_name.toPlainText()
            self.lists[index].task_list.currentItem().setText(new_name)
            self.save_user_lists_items(notes)
        except:
            self.task_window.window.close()
        else:
            self.task_window.window.close() 
        
    #Delete current task    
    def delete_task(self,item,item_no,index):
        confirm = QtWidgets.QMessageBox.question(window, 'Delete Task', 'Are you sure you want to delete this task?', 
                                                 QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        
        if confirm == QtWidgets.QMessageBox.Yes:
            #remove item from current list
            self.lists[index].task_list.takeItem(item_no)
            #remove item from other lists it was copied into  
            if self.lists[0].task_list.findItems(item, QtCore.Qt.MatchExactly):
                self.lists[0].task_list.takeItem(item_no)
                
            if self.lists[1].task_list.findItems(item, QtCore.Qt.MatchExactly):
                self.lists[1].task_list.takeItem(item_no)
                
            if self.lists[2].task_list.findItems(item, QtCore.Qt.MatchExactly):
                self.lists[2].task_list.takeItem(item_no)
            
            if self.lists[3].task_list.findItems(item, QtCore.Qt.MatchExactly):
                self.lists[3].task_list.takeItem(item_no)    
            self.task_window.window.close()
          
    #Cancel any changes made to current task
    def cancel_task_edit(self,item,item_no):
        if self.lists[0].task_list.findItems(item, QtCore.Qt.MatchExactly):
            self.lists[0].task_list.takeItem(item_no)
                
        if self.lists[1].task_list.findItems(item, QtCore.Qt.MatchExactly):
            self.lists[1].task_list.takeItem(item_no)
         
        if self.lists[3].task_list.findItems(item, QtCore.Qt.MatchExactly):
            self.lists[3].task_list.takeItem(item_no)

        self.task_window.window.close()
        
    #Opens task editing window
    def open_task_window(self): 
        index = self.MainWindow.currentIndex()
        item = self.lists[index].task_list.currentItem().text()
        item_no = self.lists[index].task_list.currentRow() 
        self.task_window = Task_Window(self.font)
        self.task_window.task_name.setPlainText(f"{item}")
        self.task_window.important.clicked.connect(lambda:self.mark_task_as_important(item))
        self.task_window.add_today.clicked.connect(lambda:self.add_to_today(item))
        self.task_window.completed.clicked.connect(lambda:self.mark_as_completed(item,item_no,index))
        self.task_window.save.clicked.connect(lambda: self.save_task(index))
        self.task_window.cancel.clicked.connect(lambda:self.cancel_task_edit(item,item_no))
        self.task_window.delete_task.clicked.connect(lambda:self.delete_task(item,item_no,index))
        self.task_window.window.show()
               
    #Saves all lists to the database
    def save_user_buttons(self):
        self.lists_manager.cursor.execute('DELETE FROM lists;')
        
        for index in range(len(self.new_lists)):
            self.lists_manager.add_list(self.new_lists[index])
            
    #Copies all lists from the database       
    def fetch_user_buttons(self):
        self.lists_manager.cursor.execute('SELECT * FROM lists;')
        buttons = self.lists_manager.get_lists()
        
        if len(buttons) > 7:
            for button in buttons[7:]:
                self.new_lists.append(str(button[1]))
       
    #Saves  the contents of all the lists into the database       
    def save_user_lists_items(self,notes):
        self.lists_manager.cursor.execute('DELETE FROM tasks;')
        
        for index in range(len(self.lists)):
            items = []
            
            for id in range((self.lists[index].task_list).count()):
                items.append((self.lists[index].task_list).item(id))
                
            for item in items:
                self.lists_manager.add_task(index,str(item.text()),str(notes))
                                        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    ui = Main_Window(window)
    window.show()
    sys.exit(app.exec_())
