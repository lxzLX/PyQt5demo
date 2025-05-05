import sys
import random
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QProgressBar, QPushButton, QWidget, QMessageBox

class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.ui_init()
        self.slot_init()

    def ui_init(self):
        self.setWindowTitle('进度条-资源模拟下载')
        self.prossBar = QProgressBar(self)
        self.prossBar.setGeometry(100, 30, 300, 30)
        self.prossBar.setRange(0, 100)
        self.prossBar.setValue(0)
        self.btn = QPushButton('开始下载', self)
        self.btn.setGeometry(150, 80, 150, 30)

    def slot_init(self):
        self.btn.clicked.connect(self.download)
        self.timer = QTimer(self)
        #设置时间间隔为1000ms，每隔1000ms触发timeout()函数,执行一次槽函数
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.update_progress)

    def update_progress(self):
        #模拟下载进度
        self.rand_num=random.randint(1, 10)
        self.cur_progress = self.prossBar.value()
        self.prossBar.setValue(self.cur_progress + self.rand_num)
        if self.cur_progress + self.rand_num >= 100:
            #下载完成
            self.prossBar.setValue(100)
            self.timer.stop()
            self.btn.setText('下载完成')
            QMessageBox.information(self, '提示', '下载完成！')

    def download(self):
        if self.btn.text() == '开始下载':
            #定时器打开
            self.timer.start()
            self.btn.setText('暂停下载')
        else:
            #定时器关闭
            self.timer.stop()
            self.btn.setText('开始下载')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Widget()
    w.show()
    sys.exit(app.exec_())