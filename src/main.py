#!/usr/bin/env python3
import json # JSON functions
import ch_api as ch # CollegeHumor API functions
import gui # GUI functions

video = ch.Video("7017501/last-jake-and-amir-episode-ever")

video_dict = video.get().json() # returns a Dictionary of the JSON returned by
                                # the CH API

gui = gui.Gui(video_dict["title"])
gui.size(800, 600)
gui.run()
