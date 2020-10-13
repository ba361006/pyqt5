import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        self._password="123"
        self.initUI()



    def initUI(self):

        self.setGeometry(300, 300, 500,500)
        self.setWindowTitle('Simple password')


        # Create textbox
        self.password_textbox = QLineEdit(self)
        self.password_textbox.setEchoMode(QLineEdit.Password)
        self.password_textbox.move(20,20)
        self.password_textbox.resize(280,40)

        #pressed
        self.password_textbox.returnPressed.connect(self.onPressed)

        # Create a enter_button in the window
        self.enter_button = QPushButton('enter', self)
        self.enter_button.move(20,80)

        # connect enter_button to function on_click
        self.enter_button.clicked.connect(self.onClick)

        self.show()   

    def closeEvent(self, event):
        event.ignore() 
    
    def onClick(self):
        textbox_value = self.password_textbox.text()
        if textbox_value == self._password :
            self.deleteLater()
        else:
            QMessageBox.question(self, "Error, please try again", "Error Message" , QMessageBox.Ok, QMessageBox.Ok)
        self.password_textbox.setText("")
    
    def onPressed(self):
        self.onClick()
    

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec_())