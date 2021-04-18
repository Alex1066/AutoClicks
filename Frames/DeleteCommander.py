import os
import tkinter as tk


def get_number_of_commanders():
    return str(len([file for file in os.listdir("Commanders")]))


class DeleteCommander(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.canvas = tk.Canvas(self, height=500, width=500, bg="#12454C")
        self.message = ""
        self.label1 = tk.Label(self.canvas,text="", bg="#12454C")
        self.var1 = tk.IntVar()
        self.radio1 = tk.Radiobutton(self.canvas, text="Delete all", value=1, bg="#12454C", variable=self.var1,
                                     activebackground="#12454C")
        self.radio2 = tk.Radiobutton(self.canvas, text="Delete last", value=2, bg="#12454C", variable=self.var1,
                                     activebackground="#12454C")
        self.delete_btn = tk.Button(self.canvas, text="Delete", command=self.delete)
        self.back = tk.Button(self.canvas, text="Back", command=self.go_back)
        self.back.place(x=225, y=400)
        self.initial_phase()

    def initial_phase(self):
        self.canvas.pack()
        self.message = "Now you have " + get_number_of_commanders() + " commandants. Do you\n" \
                                                                      "want to delete the last or all of them?"
        self.label1['text'] = self.message
        self.label1.place(x=100, y=50)
        self.radio1.place(x=100, y=100)
        self.radio2.place(x=100, y=130)
        self.delete_btn.place(x=215, y=250)

    def delete(self):
        selection = self.var1.get()
        if selection == 1:
            for f in os.listdir("Commanders"):
                os.remove("Commanders/"+f)
        if selection == 2:
            name = "commander" + get_number_of_commanders()
            os.remove("Commanders/" + name + ".txt")
        self.label1.place_forget()
        self.radio1.place_forget()
        self.radio2.place_forget()
        self.initial_phase()

    # def after_delete(self):

    def go_back(self):
        self.controller.show_frame("MenuPage")
        self.initial_phase()
