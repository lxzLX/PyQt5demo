import sys
from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtGui import QCursor

if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=QWidget()
    window.setWindowTitle("居中的窗口")

    #监视当前光标所在的那个显示器
    cursor_pos=QCursor.pos()
    print(cursor_pos)
    #把鼠标的位置传入app,screenAt()方法返回当前光标所在的显示器
    current_screen = app.screenAt(cursor_pos)

    if current_screen is not None:
        #获取当前显示器的几何信息
        screen_rect = current_screen.availableGeometry()
        print(f"屏幕尺寸: {screen_rect}")
        width = screen_rect.width()*0.5
        height = screen_rect.height()*0.5
        #设置窗口大小
        window.resize(int(width),int(height))
        #设置窗口居中
        x=screen_rect.center().x()-width/2
        y=screen_rect.center().y()-height/2
        window.move(int(x),int(y))
    window.show()
    app.exec()
