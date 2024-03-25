from PyQt5 import QtGui, QtWidgets

class Page():
    def __init__(self,font, title_font):
        super().__init__()
        #Layout settings
        self.page = QtWidgets.QWidget()
        self.grid_layout = QtWidgets.QGridLayout(self.page)
        spacer = QtWidgets.QSpacerItem(173, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.grid_layout.addItem(spacer, 0, 1, 1, 1)
        
        #List title setup
        self.list_title = QtWidgets.QLabel(self.page)
        self.list_title.setFont(title_font)
        self.grid_layout.addWidget(self.list_title, 0, 0, 1, 1)
        
        #Add new task edit box
        self.new_task_edit = QtWidgets.QLineEdit(self.page)
        self.new_task_edit.setPlaceholderText("New task")
        self.new_task_edit.setText("")
        self.new_task_edit.setFont(font)
        self.grid_layout.addWidget(self.new_task_edit, 3, 0, 1, 4)
        
        #Container for list items
        self.task_list = QtWidgets.QListWidget(self.page)
        self.task_list.setFont(font)
        self.task_list.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.grid_layout.addWidget(self.task_list, 1, 0, 1, 4)
        
        #Button to clear list contents
        self.clear_list_button = QtWidgets.QPushButton(self.page)
        self.clear_list_button.setText("Clear")
        self.clear_list_button.setFont(font)
        self.grid_layout.addWidget(self.clear_list_button, 0, 2, 1, 1)
        
        #Button to delete list
        self.delete_list_button = QtWidgets.QPushButton(self.page)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icons/Icons/bin.png"))
        self.delete_list_button.setIcon(icon)
        self.delete_list_button.setFlat(True)
        self.grid_layout.addWidget(self.delete_list_button, 0, 3, 1, 1)
        
        #Button to add a new task
        self.add_task_button = QtWidgets.QPushButton(self.page)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icons/Icons/add.png"))
        self.add_task_button.setIcon(icon)
        self.add_task_button.setFlat(True)
        self.grid_layout.addWidget(self.add_task_button, 3, 3, 1, 1)
        
        #Seperator
        self.line = QtWidgets.QFrame(self.page)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.grid_layout.addWidget(self.line, 2, 0, 1, 4)
        