import sys
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QTextBrowser

class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("故宫介绍")
        self.resize(800,600)
        self.button=QPushButton(self)
        self.button.setText('故宫')
        self.button.setGeometry(20,20,100,30)
        self.content=QTextBrowser(self)
        self.content.setGeometry(20,60,760,480)
        self.button_connect()
        self.content.setText('故宫位于北京故宫博物院，是北京世界遗产之一，也是世界上最大的古代皇宫。')
        self.content.hide()

    def button_connect(self):
        self.button.clicked.connect(self.show_content)

    def show_content(self):
        if self.content.isHidden():
            self.content.show()
            self.button.setText('收起')
        else:
            self.content.hide()
            self.button.setText('故宫')


if __name__=='__main__':
    app=QApplication(sys.argv)
    w=Widget()
    w.show()
    app.exec()