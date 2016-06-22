#!/usr/bin/env python3
from sys import path
path.append('./src') # Set import path
import json # JSON functions
import ch_api as ch # CollegeHumor API functions
import gui # GUI functions

video = ch.Video("7017501/last-jake-and-amir-episode-ever")

video_dict = video.get().json() # returns a Dictionary of the JSON returned by
                                # the CH API

gui = gui.Gui(video_dict["title"])
gui.showimage(video_dict["thumbnail"])
gui.run()
