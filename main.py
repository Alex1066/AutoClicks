import tkinter as tk
from tkinter import font as tk_font

from Frames.AddCommander import AddCommander
from Frames.ClickDelay import ClickDelay
from Frames.CommanderSaved import CommanderSaved
from Frames.DeleteCommander import DeleteCommander
from Frames.JumpClicks import JumpClicks
from Frames.JumpStepsSaved import JumpStepsSaved
from Frames.MenuPage import MenuPage
from Frames.Popup import Popup
from Frames.StartAttacks import StartAttacks


class App(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tk_font.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        self.geometry("500x500")
        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (MenuPage, AddCommander, ClickDelay, CommanderSaved, DeleteCommander, StartAttacks, JumpStepsSaved,
                  JumpClicks, Popup):
            page_name = F.__name__
            frame = F(parent=self.container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("MenuPage")

    def show_frame(self, page_name):
        """Show a frame for the given page name"""
        frame = self.frames[page_name]
        frame.tkraise()


# (912, 658) -> lvl up
# (950, 586) -> something else

if __name__ == "__main__":
    app = App()
    app.mainloop()
