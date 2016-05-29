from moviepy.editor import *

video = VideoFileClip("test.mp4")

video.write_videofile("myHolidays_edited.webm",fps=25)