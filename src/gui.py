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
