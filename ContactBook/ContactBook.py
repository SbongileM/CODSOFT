from PyQt5 import QtCore, QtGui, QtWidgets
from DatabaseManager import DatabaseManager
import Assets

#Emits a signal carrying the contents of the item clicked on
class List_Signal(QtWidgets.QListWidget):
    signal = QtCore.pyqtSignal(str)
    
    def mousePressEvent(self,event):
        task = self.itemAt(event.pos())
        if task:
            self.signal.emit(task.text())
        super().mousePressEvent(event)

class mainWindow():
    def __init__(self):
        super().__init__()
        #Private containers that manage app data
        self._contact_manager = DatabaseManager()
        self._contacts = []
        
        #Window setup
        self.window = QtWidgets.QMainWindow()
        self.window.setWindowTitle("ContactBook")
        self.window.setFixedSize(393, 520)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icons/Assets/window icon.png"))
        self.window.setWindowIcon(icon)
        
        #Layout settings
        self.centralwidget = QtWidgets.QWidget(self.window)
        self.grid_layout = QtWidgets.QGridLayout(self.centralwidget)
        
        #App title
        self.title = QtWidgets.QLabel("Contact Book",self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.grid_layout.addWidget(self.title, 0, 0, 1, 1)
        
        #General font settings
        font = QtGui.QFont()
        font.setPointSize(10)
        
        #spacer
        spacer = QtWidgets.QSpacerItem(179, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.grid_layout.addItem(spacer, 0, 1, 1, 1)
        
        #Add contact button
        self.add_contact = QtWidgets.QPushButton(self.centralwidget)
        self.add_contact.setFont(font)
        self.add_contact.setStyleSheet("image: url(:/Icons/Assets/add-contact.png);")
        self.add_contact.setAutoExclusive(True)
        self.add_contact.setFlat(True)
        self.add_contact.clicked.connect(self.new_contact)
        self.grid_layout.addWidget(self.add_contact, 0, 2, 1, 1)
        
        self.horizontal_layout = QtWidgets.QHBoxLayout()
        #Search box
        self.search_box = QtWidgets.QLineEdit(self.centralwidget)
        self.search_box.setFont(font)
        self.search_box.setPlaceholderText("Search contact...")
        self.horizontal_layout.addWidget(self.search_box)
        
        #Search button
        self.search_button = QtWidgets.QPushButton(self.centralwidget)
        self.search_button.setStyleSheet("image: url(:/Icons/Assets/search.png);")
        self.search_button.setFlat(True)
        self.search_button.setAutoExclusive(True)
        self.search_button.clicked.connect(self.search_contact)
        self.horizontal_layout.addWidget(self.search_button)
        self.grid_layout.addLayout(self.horizontal_layout, 1, 0, 1, 3)
        
        #Stacked widget storing app pages
        self.app_pages = QtWidgets.QStackedWidget(self.centralwidget)
        
        #Contact list page
        self.contact_page = QtWidgets.QWidget()
        self.grid_layout_2 = QtWidgets.QGridLayout(self.contact_page)
        #Contact list
        self.contact_list = QtWidgets.QListWidget(self.contact_page)
        self.contact_list.setSortingEnabled(True)
        self.contact_list.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.contact_list.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.contact_list.itemClicked.connect(self.contact_edit)
        self.grid_layout_2.addWidget(self.contact_list, 0, 0, 1, 1)
        self.app_pages.addWidget(self.contact_page)
        
        #Search page
        self.search_page = QtWidgets.QWidget()
        self.grid_layout_3 = QtWidgets.QGridLayout(self.search_page)
        #Searched items list
        self.search_list = QtWidgets.QListWidget(self.search_page)
        self.search_list.setSortingEnabled(True)
        self.search_list.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.search_list.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.search_list.itemClicked.connect(self.contact_edit)
        self.grid_layout_3.addWidget(self.search_list, 0, 0, 1, 1)
        self.app_pages.addWidget(self.search_page)
        
        #Fetch contacts from database
        self.fetch_contacts()
        
        #Contact view page
        self.contact_view = QtWidgets.QWidget()
        self.grid_layout_4 = QtWidgets.QGridLayout(self.contact_view)
        self.horizontal_layout_2 = QtWidgets.QHBoxLayout()
        #Name widgets setup
        self.name_icon = QtWidgets.QPushButton(self.contact_view)
        self.name_icon.setFont(font)
        self.name_icon.setStyleSheet("image: url(:/Icons/Assets/name.png);")
        self.name_icon.setFlat(True)
        self.name_icon.setCheckable(False)
        self.name_icon.setEnabled(False)
        self.horizontal_layout_2.addWidget(self.name_icon)
        self.name = QtWidgets.QLineEdit(self.contact_view)
        self.name.setFont(font)
        self.name.setStyleSheet("background-color: rgb(160, 160, 160);")
        self.name.setFrame(False)
        self.name.setClearButtonEnabled(True)
        self.horizontal_layout_2.addWidget(self.name)
        self.grid_layout_4.addLayout(self.horizontal_layout_2, 0, 0, 1, 2)
        #Phone widgets setup
        self.horizontal_layout_3 = QtWidgets.QHBoxLayout()
        self.phone_icon = QtWidgets.QPushButton(self.contact_view)
        self.phone_icon.setFont(font)
        self.phone_icon.setStyleSheet("image: url(:/Icons/Assets/phone.png);")
        self.phone_icon.setFlat(True)
        self.phone_icon.setCheckable(False)
        self.phone_icon.setEnabled(False)
        self.horizontal_layout_3.addWidget(self.phone_icon)
        self.phone = QtWidgets.QLineEdit(self.contact_view)
        self.phone.setFont(font)
        self.phone.setStyleSheet("background-color: rgb(160, 160, 160);")
        self.phone.setFrame(False)
        self.phone.setClearButtonEnabled(True)
        self.horizontal_layout_3.addWidget(self.phone)
        self.grid_layout_4.addLayout(self.horizontal_layout_3, 1, 0, 1, 2)
        #Email widgets setup
        self.horizontal_layout_4 = QtWidgets.QHBoxLayout()
        self.email_icon = QtWidgets.QPushButton(self.contact_view)
        self.email_icon.setFont(font)
        self.email_icon.setStyleSheet("image: url(:/Icons/Assets/email.png);")
        self.email_icon.setFlat(True)
        self.email_icon.setCheckable(False)
        self.email_icon.setEnabled(False)
        self.horizontal_layout_4.addWidget(self.email_icon)
        self.email = QtWidgets.QLineEdit(self.contact_view)
        self.email.setFont(font)
        self.email.setStyleSheet("background-color: rgb(160, 160, 160);")
        self.email.setFrame(False)
        self.email.setClearButtonEnabled(True)
        self.horizontal_layout_4.addWidget(self.email)
        self.grid_layout_4.addLayout(self.horizontal_layout_4, 2, 0, 1, 2)
        #Name of the store widgets setup
        self.horizontal_layout_5 = QtWidgets.QHBoxLayout()
        self.store = QtWidgets.QPushButton(self.contact_view)
        self.store.setFont(font)
        self.store.setStyleSheet("image: url(:/Icons/Assets/store name.png);")
        self.store.setFlat(True)
        self.store.setCheckable(False)
        self.store.setEnabled(False)
        self.horizontal_layout_5.addWidget(self.store)
        self.store_name = QtWidgets.QLineEdit(self.contact_view)
        self.store_name.setFont(font)
        self.store_name.setStyleSheet("background-color: rgb(160, 160, 160);")
        self.store_name.setFrame(False)
        self.store_name.setClearButtonEnabled(True)
        self.horizontal_layout_5.addWidget(self.store_name)
        self.grid_layout_4.addLayout(self.horizontal_layout_5, 3, 0, 1, 2)
        #Store location widgets setup
        self.horizontal_layout_6 = QtWidgets.QHBoxLayout()
        self.pin = QtWidgets.QPushButton(self.contact_view)
        self.pin.setFont(font)
        self.pin.setStyleSheet("image: url(:/Icons/Assets/phyical address.png);\n")
        self.pin.setFlat(True)
        self.pin.setCheckable(False)
        self.pin.setEnabled(False)
        self.horizontal_layout_6.addWidget(self.pin)
        self.address = QtWidgets.QLineEdit(self.contact_view)
        self.address.setFont(font)
        self.address.setStyleSheet("background-color: rgb(160, 160, 160);")
        self.address.setFrame(False)
        self.address.setClearButtonEnabled(True)
        self.horizontal_layout_6.addWidget(self.address)
        self.grid_layout_4.addLayout(self.horizontal_layout_6, 4, 0, 1, 2)
        #Delete contact button
        self.delete = QtWidgets.QPushButton("Delete",self.contact_view)
        self.delete.setFont(font)
        self.delete.setCheckable(True)
        self.delete.setAutoExclusive(True)
        self.grid_layout_4.addWidget(self.delete, 5, 0, 1, 1)
        #Update contact details 
        self.update = QtWidgets.QPushButton("Update",self.contact_view)
        self.update.setFont(font)
        self.update.setCheckable(True)
        self.update.setAutoExclusive(True)
        self.update.clicked.connect(self.update_contact)
        self.grid_layout_4.addWidget(self.update, 5, 1, 1, 1)
        self.app_pages.addWidget(self.contact_view)
        
        #New contact view
        self.New_contact = QtWidgets.QWidget()
        self.grid_layout_5 = QtWidgets.QGridLayout(self.New_contact)
        self.horizontal_layout_7 = QtWidgets.QHBoxLayout()
        #Name widgets
        self.name_icon_ = QtWidgets.QPushButton(self.New_contact)
        self.name_icon_.setFont(font)
        self.name_icon_.setStyleSheet("image: url(:/Icons/Assets/name.png);")
        self.name_icon_.setDefault(False)
        self.name_icon_.setFlat(True)
        self.name_icon_.setCheckable(False)
        self.name_icon_.setEnabled(False)
        self.horizontal_layout_7.addWidget(self.name_icon_)
        self.name_ = QtWidgets.QLineEdit(self.New_contact)
        self.name_.setFont(font)
        self.name_.setStyleSheet("background-color: rgb(160, 160, 160);")
        self.name_.setFrame(False)
        self.name_.setClearButtonEnabled(True)
        self.name_.setPlaceholderText("Name")
        self.horizontal_layout_7.addWidget(self.name_)
        self.grid_layout_5.addLayout(self.horizontal_layout_7, 0, 0, 1, 2)
        #Phone number widgets
        self.horizontal_ayout_8 = QtWidgets.QHBoxLayout()
        self.phone_icon_ = QtWidgets.QPushButton(self.New_contact)
        self.phone_icon_.setFont(font)
        self.phone_icon_.setStyleSheet("image: url(:/Icons/Assets/phone.png);")
        self.phone_icon_.setFlat(True)
        self.phone_icon_.setCheckable(False)
        self.phone_icon_.setEnabled(False)
        self.horizontal_ayout_8.addWidget(self.phone_icon_)
        self.phone_ = QtWidgets.QLineEdit(self.New_contact)
        self.phone_.setFont(font)
        self.phone_.setStyleSheet("background-color: rgb(160, 160, 160);")
        self.phone_.setFrame(False)
        self.phone_.setClearButtonEnabled(True)
        self.phone_.setPlaceholderText("Phone")
        self.horizontal_ayout_8.addWidget(self.phone_)
        self.grid_layout_5.addLayout(self.horizontal_ayout_8, 1, 0, 1, 2)
        #Email widgets
        self.horizontal_layout_9 = QtWidgets.QHBoxLayout()
        self.email_icon_ = QtWidgets.QPushButton(self.New_contact)
        self.email_icon_.setFont(font)
        self.email_icon_.setStyleSheet("image: url(:/Icons/Assets/email.png);")
        self.email_icon_.setFlat(True)
        self.email_icon_.setCheckable(False)
        self.email_icon_.setEnabled(False)
        self.horizontal_layout_9.addWidget(self.email_icon_)
        self.email_ = QtWidgets.QLineEdit(self.New_contact)
        self.email_.setFont(font)
        self.email_.setStyleSheet("background-color: rgb(160, 160, 160);")
        self.email_.setFrame(False)
        self.email_.setClearButtonEnabled(True)
        self.email_.setPlaceholderText("Email")
        self.horizontal_layout_9.addWidget(self.email_)
        self.grid_layout_5.addLayout(self.horizontal_layout_9, 2, 0, 1, 2)
        #Store name widgets
        self.horizontal_layout_10 = QtWidgets.QHBoxLayout()
        self.store_ = QtWidgets.QPushButton(self.New_contact)
        self.store_.setFont(font)
        self.store_.setStyleSheet("image: url(:/Icons/Assets/store name.png);")
        self.store_.setFlat(True)
        self.store_.setCheckable(False)
        self.store_.setEnabled(False)
        self.horizontal_layout_10.addWidget(self.store_)
        self.store_name_ = QtWidgets.QLineEdit(self.New_contact)
        self.store_name_.setFont(font)
        self.store_name_.setStyleSheet("background-color: rgb(160, 160, 160);")
        self.store_name_.setFrame(False)
        self.store_name_.setClearButtonEnabled(True)
        self.store_name_.setPlaceholderText("Store Name")
        self.horizontal_layout_10.addWidget(self.store_name_)
        self.grid_layout_5.addLayout(self.horizontal_layout_10, 3, 0, 1, 2)
        #Store location widgets
        self.horizontal_layout_11 = QtWidgets.QHBoxLayout()
        self.pin_ = QtWidgets.QPushButton(self.New_contact)
        self.pin_.setFont(font)
        self.pin_.setStyleSheet("image: url(:/Icons/Assets/phyical address.png);\n")
        self.pin_.setFlat(True)
        self.pin_.setCheckable(False)
        self.pin_.setEnabled(False)
        self.horizontal_layout_11.addWidget(self.pin_)
        self.address_ = QtWidgets.QLineEdit(self.New_contact)
        self.address_.setFont(font)
        self.address_.setStyleSheet("background-color: rgb(160, 160, 160);")
        self.address_.setFrame(False)
        self.address_.setClearButtonEnabled(True)
        self.address_.setPlaceholderText("Address")
        self.horizontal_layout_11.addWidget(self.address_)
        self.grid_layout_5.addLayout(self.horizontal_layout_11, 4, 0, 1, 2)
        #Cancel button
        self.cancel = QtWidgets.QPushButton("Cancel",self.New_contact)
        self.cancel.setFont(font)
        self.cancel.setCheckable(True)
        self.cancel.setAutoExclusive(True)
        self.cancel.clicked.connect(self.cancel_edits)
        self.grid_layout_5.addWidget(self.cancel, 5, 0, 1, 1)
        #Add contact button
        self.save = QtWidgets.QPushButton("Save", self.New_contact)
        self.save.setFont(font)
        self.save.setCheckable(True)
        self.save.setAutoExclusive(True)
        self.save.clicked.connect(self.save_contact)
        self.grid_layout_5.addWidget(self.save, 5, 1, 1, 1)
        self.app_pages.addWidget(self.New_contact)
        self.grid_layout.addWidget(self.app_pages, 2, 0, 1, 3)
        self.window.setCentralWidget(self.centralwidget)
        #Fetch contacts saved in memory
        self.fetch_contacts()
        #Set current page to contact list
        self.app_pages.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(self.window)
        
    #Opens the new contact page  
    def new_contact(self):
        self.app_pages.setCurrentIndex(3)
      
    #Ignores and edits made and close the contact edit page
    def cancel_edits(self):
        self.app_pages.setCurrentIndex(0)  
        
    #Copies what is currently saved to the database
    def save_contacts(self):
        self._contact_manager.cursor.execute('DELETE FROM contacts;')
        
        for index in range(len(self._contacts)):
            name = (self._contacts[index])[0]
            number = (self._contacts[index])[1]
            email = (self._contacts[index])[2]
            store_name = (self._contacts[index])[3]
            address = (self._contacts[index])[4]
            
            self._contact_manager.add_contact(name,number,email,store_name,address)
            
    #Copies the contents of the database into the contacts list
    def fetch_contacts(self):
        self._contact_manager.cursor.execute('SELECT * FROM contacts;')
        contacts = self._contact_manager.get_contacts()
        
        for contact in contacts:
            if contact:
                details = f"Name: {contact[0]}\nNumber: {contact[1]}\nEmail Address: {contact[2]}\nStore: {contact[3]}\nPhysical Address: {contact[4]}"
                                
            self.contact_list.addItem(str(details))
            self._contacts.append(contact)
            
    #Search function for the search engine
    def search_contact(self):
        searched_item = self.search_box.text()
        self.app_pages.setCurrentIndex(1)
        
        self.search_list.clear()
        
        if searched_item:
            matched_items = self._contact_manager.get_contact(searched_item)
            
            for item in matched_items:
                output_txt = f"Name: {item[1]}\nNumber: {item[2]}\nEmail: {item[3]}\nStore: {item[4]}\nPhysical Address: {item[5]}"
                                
                self.search_list.addItem(output_txt)
        
    #Save contact function for the new contact view save button        
    def save_contact(self):
        name = self.name_.text()
        number = self.phone_.text()
        email = self.email_.text()
        store_name = self.store_name_.text()
        address = self.address_.text()
        
        self._contacts.append((name,number,email,store_name,address))
        self.contact_list.addItem(f"Name: {name}\nNumber: {number}\nEmail: {email}\nStore: {store_name}\nPhysical Address: {address}")
        self.save_contacts()
        self.name_.clear(),self.phone_.clear(),self.email_.clear(),self.store_name_.clear()
        self.address_.clear()
        self.app_pages.setCurrentIndex(0)
        
    #Opens contact view page for any clicked on item in the list
    def contact_edit(self):
        sender = self.window.sender()
        contact = sender.currentItem().text()
        
        for i in range(len(self._contacts)):
            if str((self._contacts[i])[2]) in contact:
                self.name.setText(str((self._contacts[i])[0]))
                self.phone.setText(str((self._contacts[i])[1]))
                self.email.setText(str((self._contacts[i])[2]))
                self.store_name.setText(str((self._contacts[i])[3]))
                self.address.setText(str((self._contacts[i])[4]))
                self.contact_list.takeItem(i)
                self._contacts.remove(self._contacts[i])
                break
        self.app_pages.setCurrentIndex(2)
        
    #Updates list of contacts
    def update_contact(self):
        name = self.name.text()
        number = self.phone.text()
        email = self.email.text()
        store_name = self.store_name.text()
        address = self.address.text()
        
        self._contacts.append((name,number,email,store_name,address))
        self.contact_list.addItem(f"Name: {name}\nNumber: {number}\nEmail: {email}\nStore: {store_name}\nPhysical Address: {address}")
        self.app_pages.setCurrentIndex(0)
        
    #Removes contact from the list of saved contacts
    #Has a bug
    def delete_contact(self):
        name = self.name.text()
        number = self.phone.text()
        email = self.email.text()
        store_name = self.store_name.text()
        address = self.address.text()
        
        for i in range(len(self.contacts)):
            if str((self._contacts[i])[0]) == name and str((self._contacts[i])[1]) == number\
                and str((self._contacts[i])[2]) == email and str((self._contacts[i])[3]) == store_name\
                    and str((self._contacts[i])[4]) == address:
                        
                        self.contact_list.takeItem(i)
                        self._contacts.remove(self._contacts[i])
    
        self.save_contacts()
        self.app_pages.setCurrentIndex(0)
              
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = mainWindow()
    ui.window.show()
    sys.exit(app.exec_())