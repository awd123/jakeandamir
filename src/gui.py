"""Provides methods for creating a GUI with Tkinter"""
import tkinter as tk

class Gui:
    def __init__(self, title="New Window"):
        self.root = tk.Tk()
        self.root.title = title

    def run(self):
        self.root.mainloop()
