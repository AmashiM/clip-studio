

from moviepy.editor import VideoFileClip, concatenate_videoclips
import os


def merge_video_files(files: list[str], targetfilename: str):
  clips: list[VideoFileClip] = [VideoFileClip(file) for file in files]
  clip = concatenate_videoclips(clips)

  cpu = os.cpu_count()
  amount = (20 - cpu) + min(len(clips), 10)
  print(f"using: {amount} threads")
  clip.write_videofile(targetfilename, threads=amount)



