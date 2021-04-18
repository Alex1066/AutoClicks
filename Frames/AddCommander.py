import tkinter as tk
from pynput import mouse
from Commander import Commander


class AddCommander(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.canvas = tk.Canvas(self, height=500, width=500, bg="#12454C")
        self.label1 = tk.Label(self.canvas, text="Time to reach the target\n(in seconds)", bg="#12454C")
        self.entry1 = tk.Entry(self.canvas, bg="#bab707")
        self.label2 = tk.Label(self.canvas, text="Returning time\n(in seconds)", bg="#12454C")
        self.entry2 = tk.Entry(self.canvas, bg="#bab707")
        self.submit = tk.Button(self.canvas, text="Submit", command=self.submit)
        self.label3 = tk.Label(self.canvas, text="Now you need to set up the steps for your commander.\n"
                                                 "Go to the map and move the application window to the side.\n"
                                                 "Once you are ready, press GO button and initiate an attack\n"
                                                 "with your chosen commander. At this point the application\n"
                                                 "will start recording your mouse clicks and save the coordinates\n"
                                                 "of the mouse, so don't do unnecessary clicks. When the attack is\n"
                                                 "sent, press the wheel button on your mouse. This will stop\n"
                                                 "the application from recording and will save your commander. At\n"
                                                 "this point the application is ready to initiate attacks with\n"
                                                 "this commander. If you misclicked throughout the process, you\n"
                                                 "can cancel this recording by pressing the right button on your\n"
                                                 "mouse. The application will stop recording, and nothing will be\n"
                                                 "saved. To restart the process press the GO button again.",
                               bg="#12454C")
        self.GO = tk.Button(self.canvas, text="GO", command=self.go)
        self.back = tk.Button(self.canvas, text="BACK", command=lambda: self.controller.show_frame("MenuPage"))
        self.back.place(x=220, y=400)
        self.initial_phase()

        self.time_going = 0
        self.time_returning = 0
        self.clicks = []
        self.mouse_listener = mouse.Listener(on_click=self.key2)

    def initial_phase(self):
        self.canvas.pack()
        self.label1.place(x=50, y=50)
        self.entry1.place(x=54, y=85)
        self.label2.place(x=70, y=115)
        self.entry2.place(x=54, y=150)
        self.submit.place(x=90, y=200)
        self.label3.place_forget()
        self.GO.place_forget()

    def key2(self, x, y, button, pressed):
        if button == mouse.Button.left and pressed:
            self.clicks.append(mouse.Controller().position)
            print(mouse.Controller().position)
        if button == mouse.Button.middle and pressed:
            self.mouse_listener.stop()
            self.mouse_listener = mouse.Listener(on_click=self.key2)
            commander = Commander(self.clicks, self.time_going, self.time_returning)
            commander.cast_to_file()
            self.time_going = 0
            self.time_returning = 0
            self.clicks = []
            self.controller.show_frame("CommanderSaved")
            self.initial_phase()
        if button == mouse.Button.right and pressed:
            self.mouse_listener.stop()
            self.mouse_listener = mouse.Listener(on_click=self.key2)
            self.clicks = []

    def submit(self):
        self.time_going = int(self.entry1.get())
        self.time_returning = int(self.entry2.get())
        self.label1.place_forget()
        self.label2.place_forget()
        self.entry1.place_forget()
        self.entry2.place_forget()
        self.submit.place_forget()
        self.entry1.delete(0, 'end')
        self.entry2.delete(0, 'end')
        self.label3.place(x=100, y=100)
        self.GO.place(x=220, y=350)

    def go(self):
        self.mouse_listener.start()
