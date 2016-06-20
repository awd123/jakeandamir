"""Provides methods for accessing videos through the CollegeHumor oEmbed API.

Classes:

Video(vid_id)
"""
import requests # Function for making and accessing HTTP requests
from urllib.parse import urlencode # URL parsing and encoding

class Video:
    def __init__(self, vid_id):
        self.vid_id = vid_id

    def get():
        """returns a Response object of the video specified by vid_id"""
        apiparams = {"url": "http://www.collegehumor.com/video/{}".format(self.vid_id)}

        r = requests.get("http://www.collegehumor.com/oembed.json", params=apiparams)

        return r
