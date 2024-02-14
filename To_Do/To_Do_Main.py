'''
Author: Sbongile Mdaki
Date:  10 February 2024
Project: GUI desktop To-Do list application for CodSoft internship

This project aims to create a user-friendly interface for a To-Do application which
will help users organize their tasks efficiently. It allows the user to create, update
and track their To-Do lists.

The current version does not have a search engine functionality. Task notes are not saved
and task name edit is only effective in the parent/residing list. The ui has a menu tab which
contains buttons used to open respective list page, but the vertical scroll bar is not
functional. The lists can be created, cleared and deleted. Each page has a functionality to 
add a new task and upon clicking the task, a task edit window pops up. The edit window has 
a functionality to mark task as important, add task to Today list or mark tasked as mastered 
which means completed. It also has save, delete and cancel task chages buttons. It uses SQLite3
to create and manage the database of the app.

'''
from PyQt5.QtWidgets import QApplication
from TaskMaster_To_Do import Main_Window

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ui = Main_Window()
    ui.window.show()
    sys.exit(app.exec_())