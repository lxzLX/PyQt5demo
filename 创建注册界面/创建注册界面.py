from sign_up_ui import Ui_Form
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QLabel, QMessageBox
import sys
from PyQt5 import QtGui, QtCore

class MyWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        # 标题
        self.setWindowTitle("注册界面")
        self.setupUi(self)
        # 初始化槽函数
        self.slot_init()
        self.ui_init()

    def ui_init(self):
        # 账号/用户名 QLabel
        self.ID_number.setMaxLength(11)
        int_validator = QtGui.QIntValidator()
        reg_exp = QtCore.QRegExp("^\d{0,11}$")
        reg_exp_validator = QtGui.QRegExpValidator(reg_exp, self.ID_number)
        self.ID_number.setValidator(int_validator)
        self.ID_number.setValidator(reg_exp_validator)
        self.ID_number.setPlaceholderText("请输入11位数字账号")
        self.password.setMaxLength(6)
        self.password.setEchoMode(QLineEdit.Password)

    def slot_init(self):
        self.button1.clicked.connect(self.reg_slot)
        self.button2.clicked.connect(self.clear_slot)

    def reg_slot(self):
        username = self.ID_number.text()
        password = self.password.text()
        if username == "" or password == "":
            # 消息提醒框
            QMessageBox.warning(self, "注册", "用户名或者密码不能为空")
        elif 0 <len(username)<11:
            QMessageBox.warning(self, "注册", "用户名输入长度不符合要求")
        elif 0 <len(password)<6:
            QMessageBox.warning(self, "注册", "密码输入长度不符合要求")
        else:
            # 将数据写入文件中
            with open("user.txt", mode="a+", encoding="utf-8") as f:
                info = username + "," + password + "\n"
                f.write(info)
                QMessageBox.warning(self, "注册", "恭喜,注册完成!")

    def clear_slot(self):
        self.ID_number.clear()
        self.password.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())