
from typing import Any
from PyQt5 import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *
import threading
from youtube_dl import YoutubeDL

class MyLogger(object):
  pass

class DownloadTab(QWidget):
  def __init__(self):
    super().__init__()


    setattr(MyLogger, "debug", self.ytdl_debug)
    setattr(MyLogger, "warning", self.ytdl_warning)
    setattr(MyLogger, "error", self.ytdl_error)

    self.YTDL_OPTIONS = {
      "format": "best",
      "outtmpl": "./videos/%(title)s.%(ext)s",
      'logger': MyLogger(),
      'progress_hooks': [self.ytdl_hook]
    }

    self.controls = QGroupBox()
    self.controls.setGeometry(QRect(0,0, 200, 200))
    self.controls.setParent(self)

    layout = QBoxLayout(QBoxLayout.Direction.TopToBottom)

    self.label = QLabel()
    self.label.setText("Youtube URL Here:")

    self.url_input = QLineEdit()
    self.url_input.setPlaceholderText("Youtube URL Here")

    self.download_button = QPushButton()
    self.download_button.setObjectName("Download Button")
    self.download_button.setText("Download")

    self.DownloadProgressBar = QProgressBar()
    self.DownloadProgressBar.setProperty("value", 0)
    self.DownloadProgressBar.setObjectName("DownloadProgressBar")

    for widget in [self.label, self.url_input, self.download_button, self.DownloadProgressBar]:
      layout.addWidget(widget, 1)

    self.controls.setLayout(layout)


    self.download_button.clicked.connect(self.downloadButtonClicked)


  def ytdl_debug(self, msg):
    pass

  def ytdl_warning(self, msg):
    pass

  def ytdl_error(self, msg):
    pass


  def downloadButtonClicked(self):
    url = self.url_input.text()
    print(url)

    with YoutubeDL(self.YTDL_OPTIONS) as ydl:
      info = ydl.extract_info(url, download=False)

      title = info.get('title')
      print(title)

      def download():
        ydl.download([url])

      t = threading.Thread(target=download)
      t.start()
      t.join()

  def ytdl_hook(self, d):
    pass
