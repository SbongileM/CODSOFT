from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(277, 364)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.task_name = QtWidgets.QLabel(Dialog)
        self.task_name.setObjectName("task_name")
        self.gridLayout.addWidget(self.task_name, 0, 0, 1, 1)
        self.add_today = QtWidgets.QPushButton(Dialog)
        self.add_today.setCheckable(True)
        self.add_today.setAutoExclusive(True)
        self.add_today.setObjectName("add_today")
        self.gridLayout.addWidget(self.add_today, 2, 0, 1, 1)
        self.save = QtWidgets.QPushButton(Dialog)
        self.save.setCheckable(True)
        self.save.setAutoExclusive(True)
        self.save.setObjectName("save")
        self.gridLayout.addWidget(self.save, 7, 2, 1, 1)
        self.important = QtWidgets.QPushButton(Dialog)
        self.important.setCheckable(True)
        self.important.setAutoExclusive(True)
        self.important.setObjectName("important")
        self.gridLayout.addWidget(self.important, 1, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(176, 71, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 6, 0, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 3, 0, 1, 1)
        self.cancel = QtWidgets.QPushButton(Dialog)
        self.cancel.setCheckable(True)
        self.cancel.setAutoExclusive(True)
        self.cancel.setObjectName("cancel")
        self.gridLayout.addWidget(self.cancel, 7, 1, 1, 1)
        self.delete_task = QtWidgets.QPushButton(Dialog)
        self.delete_task.setCheckable(True)
        self.delete_task.setAutoExclusive(True)
        self.delete_task.setObjectName("delete_task")
        self.gridLayout.addWidget(self.delete_task, 0, 2, 1, 1)
        self.task_notes = QtWidgets.QLabel(Dialog)
        self.task_notes.setObjectName("task_notes")
        self.gridLayout.addWidget(self.task_notes, 4, 0, 1, 1)
        self.notes_edit = QtWidgets.QTextEdit(Dialog)
        self.notes_edit.setMaximumSize(QtCore.QSize(300, 700))
        self.notes_edit.setObjectName("notes_edit")
        self.gridLayout.addWidget(self.notes_edit, 5, 0, 1, 3)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.task_name.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Task</span></p></body></html>"))
        self.add_today.setText(_translate("Dialog", "Add to Today"))
        self.save.setText(_translate("Dialog", "Save"))
        self.important.setText(_translate("Dialog", " Mark as important"))
        self.cancel.setText(_translate("Dialog", "Cancel"))
        self.delete_task.setText(_translate("Dialog", "Delete"))
        self.task_notes.setText(_translate("Dialog", "Add notes"))

import Assets


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
