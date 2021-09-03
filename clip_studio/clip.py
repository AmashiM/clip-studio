
from typing import Any
from PyQt5 import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *
import os
from random import choice
from moviepy.editor import VideoFileClip, VideoClip


class ClipTab(QWidget):
  def __init__(self):
    super().__init__()

    for file in os.listdir("./clips/"):
      new_name = f"./clips/{file}"
      new_name = new_name.replace(" ", "_")
      new_name = new_name.replace("'", "")
      new_name = new_name.lower()
      os.rename(f"./clips/{file}", new_name)

    self.selected_file = None

    self.container = QGroupBox()

    self.open_file = QPushButton()
    self.open_file.setText("open file")
    self.open_file.clicked.connect(self.openFile)

    self.selected_label = QLabel()
    self.selected_label.setGeometry(QRect(0, 50, self.width(), 22))
    self.selected_label.setParent(self)

    self.start_time = QLineEdit()
    self.start_time.setPlaceholderText("Start Time")
    self.start_time.setGeometry(QRect(0, 75, int(self.width() / 2), 22))
    self.start_time.setObjectName("startTime")

    self.duration = QLineEdit()
    self.duration.setPlaceholderText("Duration")
    self.duration.setGeometry(QRect(0, 100, int(self.width() / 2), 22))
    self.duration.setObjectName("duration")

    self.clipSubmit = QPushButton()
    self.clipSubmit.setObjectName("clipSubmit")
    self.clipSubmit.setGeometry(QRect(0, 125, int(self.width() / 2), 22))
    self.clipSubmit.setText("Clip Submit")

    def makeClip() -> None:
      if self.selected_file is None:
        return

      fileName = self.selected_file.fileName()
      type1 = ''
      if fileName in os.listdir("./videos/"):
        type1 = "videos"
      fileName = f"./{type1}/{fileName}"

      characters = list('qwertyuiopasdfghjklzxcvbnmQWERTIOPASDFGHJKLZXCVBNM')
      id = './clips/'
      for i in range(25):
        id += choice(characters)
      id += self.selected_file.fileName()

      _start = float(self.start_time.text())

      _end = float(self.duration.text())

      _end = _end - _start

      _clip = VideoFileClip(fileName)

      new_clip: VideoClip = _clip.subclip(_start, _start + _end)

      new_clip.write_videofile(id)

    self.clipSubmit.clicked.connect(makeClip)

    layout = QBoxLayout(QBoxLayout.Direction.TopToBottom)
    for widget in [
      self.open_file,
      self.selected_label,
      self.start_time,
      self.duration,
      self.clipSubmit
    ]:
      layout.addWidget(widget)

    self.container.setLayout(layout)

    self.container.setParent(self)


  @property
  def compileFileName(self) -> str:
    number = len(os.listdir("./compilations/"))
    characters = 'qwertyuiopasdfghjklzxcvbnmQWERTIOPASDFGHJKLZXCVBNM'.split()
    id = ''
    for i in range(5):
      id += choice(characters)

    return f"./compilations/compilation{number}.mp4"


  def openFile(self):
    fileName, _ = QFileDialog.getOpenFileName(parent=self, caption="Open Movie", directory=QDir.currentPath())

    if fileName != '':
      self.selected_file = QUrl.fromLocalFile(fileName)
      self.selected_label.setText(self.selected_file.fileName())
