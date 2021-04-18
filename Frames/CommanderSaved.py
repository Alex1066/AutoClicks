import tkinter as tk


class CommanderSaved(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.canvas = tk.Canvas(self, height=500, width=500, bg="#12454C")
        self.canvas.pack()
        self.label1 = tk.Label(self.canvas, text="Congratulations! Your commander was successfully added.\n"
                                                 "Now you can go back to the menu and add more or start an\n"
                                                 "attack. Good luck!",
                               bg="#12454C")
        self.label1.place(x=100, y=100)
        self.submit = tk.Button(self.canvas, text="MENU", command=lambda: self.controller.show_frame("MenuPage"))
        self.submit.place(x=220, y=400)
