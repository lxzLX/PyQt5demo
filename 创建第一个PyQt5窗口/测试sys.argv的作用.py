from PyQt5.Qt import *
import sys

print(sys.argv)

#创建QApplication实例
app = QApplication(sys.argv)

print(app.arguments())