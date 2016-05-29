from random import randint
import random
from moviepy.editor import *

video = VideoFileClip("test.mp4")

inputVideoDuration = int(video.duration)
outputVideoDuration = 75

print inputVideoDuration

narrativeArray = []
editTimesArray = []

for x in range (0, outputVideoDuration):
    randTimeInSec = randint(0, inputVideoDuration - 1)

    while randTimeInSec in editTimesArray:
        randTimeInSec = randint(0, inputVideoDuration - 1)

    editTimesArray.append(randTimeInSec)

editTimesArray = sorted(editTimesArray)

for x in range (0, len(editTimesArray)):
    randTimeInSec = editTimesArray[x]
    randClipDuration = random.uniform(0.5, 1.0)

    videoClip = video.subclip(randTimeInSec, randTimeInSec + randClipDuration)
    narrativeArray.append(videoClip)

finalVideo = concatenate_videoclips(narrativeArray)

finalVideo.write_videofile("test_edited.mp4",fps=25)