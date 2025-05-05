import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

class MusicPlayer(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.slot_init()

    def initUI(self):
        self.setWindowTitle('音乐播放器')
        self.btn = QPushButton('播放', self)
        self.btn.setGeometry(100, 50, 100, 40)
        self.player = QMediaPlayer()
        self.player.setMedia(QMediaContent(QUrl.fromLocalFile("./music/凤凰传奇 - 最炫民族风.mp3")))
        print(f"QtMultimedia 是否可用？{self.player.isAvailable()}")  # 应输出 True

    def slot_init(self):
        self.btn.clicked.connect(self.play_music)

    def play_music(self):
        if self.player.state()==QMediaPlayer.PlayingState:
            self.player.pause()
            self.btn.setText('播放')
        else:
            self.player.play()
            self.btn.setText('暂停')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    player = MusicPlayer()
    player.show()
    sys.exit(app.exec_())