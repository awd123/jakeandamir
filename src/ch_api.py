"""Provides methods for accessing videos through the CollegeHumor oEmbed API.

Functions:

getvideo(vid_id) -- returns a Response object of the video specified by vid_id
"""
import requests # Function for making and accessing HTTP requests
from urllib.parse import urlencode # URL parsing and encoding

def getvideo(vid_id):
    apiparams = {"url": "http://www.collegehumor.com/video/{}".format(vid_id)}

    r = requests.get("http://www.collegehumor.com/oembed.json", params=apiparams)

    return r
