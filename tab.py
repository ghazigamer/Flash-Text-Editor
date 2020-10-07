from tkinter import *
from tkinter import ttk
from textconfig import *


class Tab:
    def __init__(self, master):
        self.notebook = ttk.Notebook(master)
        self.txt_collection = []

    def add_tab(self, title):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text=title)
        self.txt = Text(
            frame,
            undo=True,
            insertbackground=txtconfig.insertbackground,
            background=txtconfig.background,
            foreground=txtconfig.foreground,
            selectbackground=txtconfig.selectbackground,
        )
        self.txt.config(font=(txtconfig.font_family, txtconfig.font_size))
        self.txt_collection.append(self.txt)
        return self.txt, self.notebook