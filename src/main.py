#!/usr/bin/env python3
import json # JSON functions
import ch_api as ch # CollegeHumor API functions

video = ch.Video("7017501/last-jake-and-amir-episode-ever")

video_dict = video.get().json() # returns a Dictionary of the JSON returned by
                                # the CH API

print(video_dict["title"])
