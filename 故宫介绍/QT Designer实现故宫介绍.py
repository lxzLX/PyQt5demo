from 故宫介绍.my_window_ui import Ui_Form
from PyQt5.QtWidgets import QApplication, QWidget
import sys

class MyWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("故宫介绍")
        self.slot_init()
        self.content.hide()
        self.content.setText("故宫位于北京东三环，是北京世界遗产名胜区，是京城著名的皇宫。")

    def slot_init(self):
        self.button.clicked.connect(self.show_info)

    def show_info(self):
        if self.content.isHidden():
            self.content.show()
            self.button.setText("隐藏")
        else:
            self.content.hide()
            self.button.setText("显示")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec()
