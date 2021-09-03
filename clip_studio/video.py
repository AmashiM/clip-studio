
from typing import Any
from PyQt5 import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *

class VideoPlayer(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt5 Video Player")

        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        videoWidget = QVideoWidget()

        self.playButton = QPushButton()
        self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.playButton.clicked.connect(self.play)

        self.duration = QLabel()
        self.duration.setStyleSheet("border: 1px solid black;")
        def updateDurationLabel():
          self.duration.setText("end: " + str(self.mediaPlayer.duration() / 1000))
        self.mediaPlayer.durationChanged.connect(updateDurationLabel)

        self.position = QLabel()
        self.position.setStyleSheet("border: 1px solid black;")
        def updatePositionLabel():
          self.position.setText("pos: " + str(self.mediaPlayer.position() / 1000))
        self.mediaPlayer.positionChanged.connect(updatePositionLabel)

        self.controls = QGroupBox()


        self.openButton = QPushButton("Open Video")
        self.openButton.clicked.connect(self.openFile)

        self.input_pos = QLineEdit()

        self.set_pos = QPushButton()
        self.set_pos.setText("Set Position")

        def updateVideoPosition():
          pos = int(self.input_pos.text())
          self.mediaPlayer.setPosition(pos)

        self.set_pos.clicked.connect(updateVideoPosition)

        control_layout = QBoxLayout(QBoxLayout.Direction.LeftToRight)
        for widget in [
          self.openButton, self.playButton, self.position, self.duration, self.input_pos, self.set_pos
          ]:
          control_layout.addWidget(widget)

        self.controls.setLayout(control_layout)


        layout = QVBoxLayout()
        layout.addWidget(videoWidget, 5)
        layout.addWidget(self.controls, 0)

        self.setLayout(layout)
        self.mediaPlayer.setVideoOutput(videoWidget)

    def openFile(self):
        fileName, _ = QFileDialog.getOpenFileName(self, "Open Movie", QDir.currentPath())

        if fileName != '':
            self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(fileName)))

    def play(self):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()
        else:
            self.mediaPlayer.play()
