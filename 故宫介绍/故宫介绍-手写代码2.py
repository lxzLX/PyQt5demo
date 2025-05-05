import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QTextBrowser


class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('故宫介绍')
        self.resize(450, 300)
        self.move(400, 400)

        # 初始化UI
        self.ui_init()
        # 初始化槽函数
        self.slot_init()

        # 默认隐藏文本框
        self.show_txt.hide()

    def ui_init(self):
        # 创建按钮
        self.show_btn = QPushButton(self)
        self.show_btn.setText('故宫')
        self.show_btn.setGeometry(10, 100, 100, 30)

        # 创建文本框组件
        self.show_txt = QTextBrowser(self)
        self.show_txt.setGeometry(200, 40, 200, 200)

        # 预先设置文本内容（但保持隐藏）
        self.show_txt.setText("故宫建筑群以中轴线为中心，布局严谨有序，体现了中国古代建筑的艺术风格和哲学思想。"
                              "屋顶上铺着黄色的琉璃瓦，在阳光下闪闪发光，显得气势磅礴；红色的墙面上，雕刻着各种图案，细节精致。"
                              "故宫的建筑风格典雅瑰丽，展现了中国古代建筑的高超技艺和独特魅力。")

    def slot_init(self):
        self.show_btn.clicked.connect(self.toggle_info)

    def toggle_info(self):
        """
        槽函数：切换文本框的显示/隐藏状态
        """
        if self.show_txt.isVisible():
            self.show_txt.hide()
            self.show_btn.setText('显示故宫介绍')
        else:
            self.show_txt.show()
            self.show_btn.setText('隐藏介绍')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Widget()
    window.show()
    sys.exit(app.exec_())