import tkinter as tk


class ClickDelay(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.canvas = tk.Canvas(self, height=500, width=500, bg="#12454C")
        self.label1 = tk.Label(self.canvas, text="Set a delay between click(in seconds).\n"
                                                 "The game has a slow respond time, therefore\n"
                                                 "a small delay is needed. This is also hardware\n"
                                                 "dependant. The default delay is 1 seconds. You\n"
                                                 "can either increase if the computer is slower, or\n"
                                                 "decrease if it is faster. Though it is not recommended\n"
                                                 "to be lower than 0.5. ", bg="#12454C")
        self.entry1 = tk.Entry(self.canvas, bg="#bab707")
        self.submit = tk.Button(self.canvas, text="Submit", command=self.submit)
        self.label2 = tk.Label(self.canvas, text="The delay was set.", bg="#12454C")
        self.back = tk.Button(self.canvas, text="Back", command=self.go_back)
        self.back.place(x=225, y=400)
        self.initial_phase()

    def initial_phase(self):
        self.canvas.pack()
        self.label1.place(x=100, y=50)
        self.entry1.place(x=180, y=200)
        self.submit.place(x=215, y=250)
        self.label2.place_forget()

    def submit(self):
        self.set_delay()
        self.label1.place_forget()
        self.entry1.place_forget()
        self.entry1.delete(0, 'end')
        self.submit.place_forget()
        self.label2.place(x=200, y=100)

    def go_back(self):
        self.controller.show_frame("MenuPage")
        self.initial_phase()
        
    def set_delay(self):
        f = open("Others/Delay", "w")
        f.write(self.entry1.get())
        f.close()
