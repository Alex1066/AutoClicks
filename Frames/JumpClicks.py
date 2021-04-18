import tkinter as tk
from pynput import mouse


class JumpClicks(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.canvas = tk.Canvas(self, height=500, width=500, bg="#12454C")
        self.label1 = tk.Label(self.canvas, text="Here you need to set the clicks for the jump time after\n"
                                                 "the camp was attacked. Move the application window to the\n"
                                                 "side and press go button, then do the jump. The application\n"
                                                 "will start recording your mouse clicks. When you are ready\n"
                                                 "press the wheel button on the mouse, and jump will be saved.\n"
                                                 "If you made a mistake, press the right button on the mouse,\n"
                                                 "and you can restart by pressing go one more time.",
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
        f = open("Others/Jump", "w")
        for click_position in self.clicks:
            clicks += str(click_position[0]) + ',' + str(click_position[1]) + ' '
        f.write(clicks)
        f.close()

    def key2(self, x, y, button, pressed):
        if button == mouse.Button.left and pressed:
            self.clicks.append(mouse.Controller().position)
        if button == mouse.Button.middle and pressed:
            self.mouse_listener.stop()
            self.mouse_listener = mouse.Listener(on_click=self.key2)
            self.save()
            self.clicks = []
            self.controller.show_frame("JumpStepsSaved")
        if button == mouse.Button.right and pressed:
            self.mouse_listener.stop()
            self.mouse_listener = mouse.Listener(on_click=self.key2)
            self.clicks = []

    def go(self):
        self.mouse_listener.start()
