"""Provides methods for creating a GUI with Tkinter"""
import tkinter as tk
from PIL import Image, ImageTk

class Gui:
    def __init__(self, title="New Window"):
        self.root = tk.Tk()
        self.root.title(title)

    def size(self, width, height, offsetx=0, offsety=0):
        self.root.geometry("{}x{}+{}+{}".format(width, height,
                                                offsetx, offsety))

    def run(self):
        self.root.mainloop()

    def showimage(self, imageurl, _offsetx=0, _offsety=0, resize=True):
        imagetk = ImageTk.PhotoImage(Image.Open(imageurl))

        width   = imagetk.width()
        height  = imagetk.height()
        offsetx = _offsetx
        offsety = _offsety

        if resize: self.size(width, height, offsetx, offsety)

        imagepanel = tk.Label(self.root, image=imagetk)
        imagepanel.pack(side='top', fill='both', expand='yes')

        imagepanel.image = imagetk
