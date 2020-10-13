import sys
from PyQt5.QtWidgets import *


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):               

        self.resize(400,400)
        self.center()

        self.setWindowTitle('Center')    
        self.show()


    def center(self):
        #获得主窗口所在的框架
        qr = self.frameGeometry()
        #获取显示器的分辨率，然后得到屏幕中间点的位置。
        cp = QDesktopWidget().availableGeometry().center()
        
        #然后把主窗口框架的中心点放置到屏幕的中心位置。
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        
        


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())