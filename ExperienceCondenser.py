from random import randint
import random
from moviepy.editor import *
import os
import easygui

def edit_video(videoFileLocation):
    video = VideoFileClip(videoFileLocation)

    input_video_duration = int(video.duration)
    output_video_duration = 75

    narrative_array = []
    edit_times_array = []

    for x in range(0, output_video_duration):
        rand_time_in_sec = randint(0, input_video_duration - 1)

        while rand_time_in_sec in edit_times_array:
            rand_time_in_sec = randint(0, input_video_duration - 1)

        edit_times_array.append(rand_time_in_sec)

    edit_times_array = sorted(edit_times_array)

    for x in range(0, len(edit_times_array)):
        rand_time_in_sec = edit_times_array[x]
        rand_clip_duration = random.uniform(0.5, 1.0)

        video_clip = video.subclip(rand_time_in_sec, rand_time_in_sec + rand_clip_duration)
        narrative_array.append(video_clip)

    final_video = concatenate_videoclips(narrative_array)

    newFileName = os.path.splitext(videoFileLocation)[0] + "_edited" + os.path.splitext(videoFileLocation)[1]

    final_video.write_videofile(newFileName, fps=25)

edit_video("test.mp4")

