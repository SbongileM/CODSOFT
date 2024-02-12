from PyQt5 import QtGui, QtWidgets

class Page():
    def __init__(self,font, title_font):
        super().__init__()
        self.page = QtWidgets.QWidget()
        self.grid_layout = QtWidgets.QGridLayout(self.page)
        
        self.list_title = QtWidgets.QLabel(self.page)
        self.list_title.setFont(title_font)
        self.grid_layout.addWidget(self.list_title, 0, 0, 1, 1)
        
        spacer = QtWidgets.QSpacerItem(173, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.grid_layout.addItem(spacer, 0, 1, 1, 1)
        
        self.new_task_edit = QtWidgets.QLineEdit(self.page)
        self.new_task_edit.setPlaceholderText("New task")
        self.new_task_edit.setFont(font)
        self.grid_layout.addWidget(self.new_task_edit, 3, 0, 1, 2)
        
        self.task_list = QtWidgets.QListWidget(self.page)
        self.task_list.setFont(font)
        self.task_list.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.grid_layout.addWidget(self.task_list, 1, 0, 1, 3)
        
        self.clear_list_button = QtWidgets.QPushButton(self.page)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icons/Icons/bin.png"))
        self.clear_list_button.setIcon(icon)
        self.clear_list_button.setCheckable(True)
        self.clear_list_button.setAutoExclusive(True)
        self.clear_list_button.setFlat(True)
        self.grid_layout.addWidget(self.clear_list_button, 0, 2, 1, 1)
        
        self.add_task_button = QtWidgets.QPushButton(self.page)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icons/Icons/add.png"))
        self.add_task_button.setIcon(icon)
        self.add_task_button.setCheckable(True)
        self.add_task_button.setFlat(True)
        self.grid_layout.addWidget(self.add_task_button, 3, 2, 1, 1)
        
        self.line = QtWidgets.QFrame(self.page)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.grid_layout.addWidget(self.line, 2, 0, 1, 3)