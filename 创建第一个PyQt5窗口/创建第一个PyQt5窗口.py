import sys
from PyQt5.QtWidgets import QApplication, QWidget


if __name__ =='__main__':
    # 创建一个QApplication实例
    app = QApplication(sys.argv)
    # 创建一个QWidget实例
    window = QWidget()
    window.setWindowTitle('Hello PyQt5')
    window.resize(800, 600)
    window.move(500, 500)

    #显示窗口
    window.show()
    app.exec_()