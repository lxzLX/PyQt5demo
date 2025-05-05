from 图像显示 import Ui_Form
import sys
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget


class window(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.slot_init()
        self.label1.hide()
        # self.label2.hide()

        # self.move=QtGui.QMovie("../images/fan.gif")
        # self.label2.setScaledContents(True)
        # self.label2.setMovie(self.move)
        print(self.label1.isVisible())
        print(self.label1.size())
        print("label2 大小：", self.label2.size())
        self.label1.setStyleSheet("border: 1px solid red")
        self.label2.setStyleSheet("border: 1px solid green")

    def slot_init(self):
        self.btn1.clicked.connect(self.show_pic)
        self.btn2.clicked.connect(self.show_gif)

    def show_pic(self):
        #self.label1.setPixmap(QPixmap(r"D:\python-learn\PyQt5demo\images\light_on.jpg").scaled(self.label1.size()))
        #self.label1.setPixmap(QPixmap("../images/background.png").scaled(self.label1.size()))
        self.label1.setVisible(not self.label1.isVisible())
        print(self.label1.isVisible())

    def show_gif(self):
        # visible=self.label2.isVisible()
        # self.label2.setVisible(not visible)
        # if visible:
        #     self.move.start()
        # else:
        #     self.move.stop()
        movie = QtGui.QMovie()
        #movie.setFileName(r"D:\python-learn\PyQt5demo\images\fan.gif")
        movie.setFileName("../images/fan.gif")
        # 标签内容自适应
        self.label2.setScaledContents(True)
        # 给标签设置动图
        self.label2.setMovie(movie)
        # 启动动画
        movie.start()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = window()
    w.show()
    sys.exit(app.exec_())

    # QT_QPA_PLATFORM_PLUGIN_PATH
    # D:\人工智能实验平台\FS_AISIMS\tools\Python\Lib\site - packages\PyQt5\Qt\plugins\platforms