from PyQt5 import QtCore, QtWidgets, QtGui
import Assets

class Task_Window():
    def __init__(self,task,font):
        super().__init__()
        #Window setup
        self.window = QtWidgets.QMainWindow()
        self.window.setWindowTitle("Task Edit Window")
        self.window.setFixedSize(290, 460)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icons/Icons/To-do.png"))
        self.window.setWindowIcon(icon)
        
        #Layout settings
        self.centralwidget = QtWidgets.QWidget(self.window)
        self.grid_layout = QtWidgets.QGridLayout(self.centralwidget)
        spacer = QtWidgets.QSpacerItem(176, 71, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.grid_layout.addItem(spacer, 7, 0, 1, 2)
        spacer1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.grid_layout.addItem(spacer1, 4, 0, 1, 1)

        #Task name label setup
        self.task_name = QtWidgets.QTextEdit(self.window)
        self.task_name.setMaximumSize(QtCore.QSize(300,50))
        self.task_name.setStyleSheet("background-color: rgb(240, 240, 240);\n"
                                    "font-size:14pt; font-weight:400;")
        self.task_name.setText(f"{task}")
        self.task_name.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.grid_layout.addWidget(self.task_name, 0, 0, 1, 3)
        
        #Button adds current item to Today list
        self.add_today = QtWidgets.QPushButton(self.window)
        self.add_today.setText("Add to Today")
        self.add_today.setFont(font)
        self.add_today.setCheckable(True)
        self.add_today.setAutoExclusive(True)
        self.grid_layout.addWidget(self.add_today, 1, 0, 1, 3)
        
        #Save task edit changes
        self.save = QtWidgets.QPushButton(self.window)
        self.save.setText("Save")
        self.save.setFont(font)
        self.save.setCheckable(True)
        self.grid_layout.addWidget(self.save, 8, 2, 1, 1)
        
        #Button adds current item to the list of important items
        self.important = QtWidgets.QPushButton(self.window)
        self.important.setText("Mark as Important")
        self.important.setFont(font)
        self.important.setCheckable(True)
        self.important.setAutoExclusive(True)
        self.grid_layout.addWidget(self.important, 2, 0, 1, 3)
        
        #Button adds current item to the list of important items
        self.completed = QtWidgets.QPushButton(self.window)
        self.completed.setText("Mark as Mastered")
        self.completed.setFont(font)
        self.completed.setCheckable(True)
        self.completed.setAutoExclusive(True)
        self.grid_layout.addWidget(self.completed, 3, 0, 1, 3)
        
        #Cancel any changes made on the task edit window
        self.cancel = QtWidgets.QPushButton(self.window)
        self.cancel.setText("Cancel")
        self.cancel.setFont(font)
        self.cancel.setCheckable(True)
        self.grid_layout.addWidget(self.cancel, 8, 1, 1, 1)
        
        #Remove selected task from selected list
        self.delete_task = QtWidgets.QPushButton(self.window)
        self.delete_task.setText("Delete")
        self.delete_task.setFont(font)
        self.grid_layout.addWidget(self.delete_task, 8, 0, 1, 1)
        
        #Additional task notes
        self.task_notes = QtWidgets.QLabel(self.window)
        self.task_notes.setText("Add notes")
        self.task_notes.setFont(font)
        self.grid_layout.addWidget(self.task_notes, 5, 0, 1, 1)
        self.notes_edit = QtWidgets.QTextEdit(self.window)
        self.notes_edit.setFont(font)
        self.notes_edit.resize(QtCore.QSize(300, 800))
        self.grid_layout.addWidget(self.notes_edit, 6, 0, 1, 3)

        self.window.setCentralWidget(self.centralwidget)
