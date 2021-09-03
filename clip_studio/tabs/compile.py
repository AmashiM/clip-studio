

from typing import Any
from PyQt5 import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *
import sys
import threading
from threading import Thread
from random import choice, shuffle
import os
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy.editor import VideoFileClip
import cv2

from Util import merge_video_files

class CompileTab(QWidget):
  def __init__(self):
    super().__init__()

    layout = QBoxLayout(QBoxLayout.Direction.TopToBottom)

    self.label = QLabel()
    self.label.setText("Use this button to merge all the clips into one big video")

    self.compileButton = QPushButton()
    self.compileButton.setText("Compile")
    self.compileButton.clicked.connect(self.compileButtonPressed)

    for widget in [self.label, self.compileButton]:
      layout.addWidget(widget, 0)

    self.setLayout(layout)

  @property
  def clips(self):
    return [ VideoFileClip(f"./clips/{file}") for file in os.listdir("./clips/") ]

  def compileButtonPressed(self):

    clips: list[VideoFileClip] = []

    for file in [f"./clips/{clip_file}" for clip_file in os.listdir("./clips/")]:
      clips.append((file))

    shuffle(clips)

    # clip = concatenate_videoclips(clips)

    # clip.write_videofile(self.compileFileName, threads=5)

    merge_video_files(clips, self.compileFileName)

  @property
  def compileFileName(self) -> str:
    number = len(os.listdir("./compilations/"))
    characters = 'qwertyuiopasdfghjklzxcvbnmQWERTIOPASDFGHJKLZXCVBNM'.split()
    id = ''
    for i in range(5):
      id += choice(characters)

    return f"./compilations/compilation{number}.mp4"
