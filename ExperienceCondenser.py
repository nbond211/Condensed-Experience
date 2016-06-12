# coding=utf-8
from random import randint, uniform
from moviepy.editor import *
import os
import cv2
import detectcolor
import getcolor


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
        rand_clip_duration = uniform(0.5, 1.0)

        video_clip = video.subclip(rand_time_in_sec, rand_time_in_sec + rand_clip_duration)
        narrative_array.append(video_clip)

    final_video = concatenate_videoclips(narrative_array)

    new_file_name = os.path.splitext(videoFileLocation)[0] + "_edited" + os.path.splitext(videoFileLocation)[1]

    final_video.write_videofile(new_file_name, fps=25)


def edit_video_with_color(videoFileLocation, color):
    video = VideoFileClip(videoFileLocation)

    input_video_duration = int(video.duration)
    output_video_duration = 75

    narrative_array = []
    edit_times_array = []
    times_seen_array = []
    count = 0

    while count < 3000 and len(edit_times_array) < output_video_duration:
        rand_time_in_sec = randint(0, input_video_duration - 1)
        print "count: " + str(count)
        print "len: " + str(len(edit_times_array))
        times_seen_array.append(rand_time_in_sec)

        while rand_time_in_sec in times_seen_array:
            rand_time_in_sec = randint(0, input_video_duration - 1)

        if is_color_in_frame(videoFileLocation, rand_time_in_sec, color):
            edit_times_array.append(rand_time_in_sec)
            count += 1
        else:
            count += 1

    edit_times_array = sorted(edit_times_array)

    for x in range(0, len(edit_times_array)):
        rand_time_in_sec = edit_times_array[x]
        rand_clip_duration = uniform(0.5, 1.0)

        video_clip = video.subclip(rand_time_in_sec, rand_time_in_sec + rand_clip_duration)
        narrative_array.append(video_clip)

    final_video = concatenate_videoclips(narrative_array)

    new_file_name = os.path.splitext(videoFileLocation)[0] + "_edited" + os.path.splitext(videoFileLocation)[1]

    final_video.write_videofile(new_file_name, fps=25)


def is_color_in_frame(video_file_location, time_in_sec, color):
    vidcap = cv2.VideoCapture(video_file_location)
    time_in_ms = time_in_sec * 1000
    vidcap.set(15, time_in_ms)

    os.system("ffmpeg -ss " + str(time_in_sec) + " -i " + video_file_location + " -t 00:00:1 -r 1 -f singlejpeg frame.jpg -y")
    colors = getcolor.get_colors("frame.jpg")

    color_in_frame = False

    for x in range (0, len(colors)):
        if detectcolor.min_color_diff((colors[x][1][0], colors[x][1][1], colors[x][1][2]))[1] == color:
            color_in_frame = True

    return color_in_frame


edit_video_with_color("bug.mp4", "YELLOW")