from PyQt5 import QtCore, QtWidgets, QtGui
import Assets

class Task_Window():
    def __init__(self, dialog):
        super().__init__()
        dialog.setWindowTitle("Task Edit Window")
        dialog.resize(277, 364)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icons/Icons/To-do.png"))
        dialog.setWindowIcon(icon)
        
        font = QtGui.QFont()
        font.setPointSize(10)
        
        self.grid_layout = QtWidgets.QGridLayout(dialog)

        self.task_name = QtWidgets.QLabel(dialog)
        self.task_name.setText("<html><head/><body><p><span style=\" \
                                font-size:14pt; font-weight:600;\"\
                                    >Task</span></p></body></html>")
        self.grid_layout.addWidget(self.task_name, 0, 0, 1, 1)
        
        self.add_today = QtWidgets.QPushButton(dialog)
        self.add_today.setText("Add to Today")
        self.add_today.setFont(font)
        self.grid_layout.addWidget(self.add_today, 2, 0, 1, 1)
        
        self.save = QtWidgets.QPushButton(dialog)
        self.save.setText("Save")
        self.save.setFont(font)
        self.grid_layout.addWidget(self.save, 7, 2, 1, 1)
        
        self.important = QtWidgets.QPushButton(dialog)
        self.important.setText("Mark as important")
        self.important.setFont(font)
        self.grid_layout.addWidget(self.important, 1, 0, 1, 1)
        
        spacer = QtWidgets.QSpacerItem(176, 71, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.grid_layout.addItem(spacer, 6, 0, 1, 2)
        spacer1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.grid_layout.addItem(spacer1, 3, 0, 1, 1)
        
        self.cancel = QtWidgets.QPushButton(dialog)
        self.cancel.setText("Cancel")
        self.cancel.setFont(font)
        self.grid_layout.addWidget(self.cancel, 7, 1, 1, 1)
        
        self.delete_task = QtWidgets.QPushButton(dialog)
        self.delete_task.setText("Delete")
        self.delete_task.setFont(font)
        self.grid_layout.addWidget(self.delete_task, 0, 2, 1, 1)
        
        self.task_notes = QtWidgets.QLabel(dialog)
        self.task_notes.setText("Add notes")
        self.task_notes.setFont(font)
        self.grid_layout.addWidget(self.task_notes, 4, 0, 1, 1)
        
        self.notes_edit = QtWidgets.QTextEdit(dialog)
        self.notes_edit.setFont(font)
        self.notes_edit.setMaximumSize(QtCore.QSize(300, 700))
        self.grid_layout.addWidget(self.notes_edit, 5, 0, 1, 3)

        QtCore.QMetaObject.connectSlotsByName(dialog)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QDialog()
    ui = Task_Window(dialog)
    dialog.show()
    sys.exit(app.exec_())
