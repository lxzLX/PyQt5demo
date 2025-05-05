import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QMessageBox, QWidget
from PyQt5.QtCore import pyqtSignal

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.slot_init()

    def initUI(self):
        self.setWindowTitle('界面切换')
        self.btn1 = QPushButton('注册', self)
        self.btn1.move(100, 100)
        self.btn2 = QPushButton('登录', self)
        self.btn2.move(100, 150)
        self.btn3 = QPushButton('退出', self)
        self.btn3.move(100, 200)
        self.registerWindow = registerWindow()
        self.loginWindow = loginWindow()

    def slot_init(self):
        self.btn1.clicked.connect(self.show_register)
        self.btn2.clicked.connect(self.show_login)
        self.btn3.clicked.connect(self.exit_close)
        self.registerWindow.send_signal.connect(self.show)
        self.loginWindow.send_signal.connect(self.show)
        self.registerWindow.send_arg_login.connect(self.loginWindow.recv_meg)

    def show_register(self):
        self.registerWindow.show()
        self.close()

    def show_login(self):
        self.loginWindow.show()
        self.close()

    def exit_close(self):
        reply = QMessageBox.question(self, '退出', '确认退出吗？', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.close()


class registerWindow(QWidget):
    send_signal = pyqtSignal()
    send_arg_login = pyqtSignal(dict)
    def __init__(self):
        super().__init__()
        self.initUI()
        self.slot_init()

    def initUI(self):
        self.setWindowTitle('注册')
        self.setGeometry(300, 200, 300, 200)
        self.btn1 = QPushButton('返回主界面', self)
        self.btn1.move(100, 100)

    def slot_init(self):
        self.btn1.clicked.connect(self.show_main_window)

    def show_main_window(self):
        self.close()
        self.send_signal.emit()
        self.send_arg_login.emit({"这是来自于注册界面的参数": 123})



class loginWindow(QWidget):
    send_signal = pyqtSignal()
    def __init__(self):
        super().__init__()
        self.initUI()
        self.slot_init()

    def initUI(self):
        self.setWindowTitle('登录')
        self.setGeometry(300, 200, 300, 200)
        self.btn1 = QPushButton('返回主界面', self)
        self.btn1.move(100, 100)

    def slot_init(self):
        self.btn1.clicked.connect(self.show_main_window)

    def show_main_window(self):
        self.close()
        # 触发信号，通知主界面切换
        self.send_signal.emit()

    def recv_meg(self, arg):
        print(f'接收到的参数：{arg}')
        print(f'字典的值：{arg["这是来自于注册界面的参数"]}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec_())

