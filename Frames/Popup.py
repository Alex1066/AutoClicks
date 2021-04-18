import tkinter as tk

from pynput import mouse


class Popup(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.canvas = tk.Canvas(self, height=500, width=500, bg="#12454C")
        self.label1 = tk.Label(self.canvas, text="Here you will let the application know how to close the\n"
                                                 "window with rewards that pops up. To do so you you only\n"
                                                 "have to press the GO button, click on the mark on the\n"
                                                 "reward window to close it.",
                               bg="#12454C")
        self.GO = tk.Button(self.canvas, text="GO", command=self.go)
        self.canvas.pack()
        self.label1.place(x=80, y=100)
        self.GO.place(x=225, y=250)
        self.back = tk.Button(self.canvas, text="BACK", command=lambda: self.controller.show_frame("MenuPage"))
        self.back.place(x=220, y=400)
        self.clicks = []
        self.mouse_listener = mouse.Listener(on_click=self.key2)

    def save(self):
        clicks = ""
        f = open("Others/Popups", "w")
        for click_position in self.clicks:
            clicks += str(click_position[0]) + ',' + str(click_position[1]) + ' '
        f.write(clicks)
        f.close()

    def key2(self, x, y, button, pressed):
        if button == mouse.Button.left and pressed:
            self.clicks.append(mouse.Controller().position)
            self.mouse_listener.stop()
            self.mouse_listener = mouse.Listener(on_click=self.key2)
            self.save()
            self.clicks = []
            self.controller.show_frame("MenuPage")

    def go(self):
        self.mouse_listener.start()
