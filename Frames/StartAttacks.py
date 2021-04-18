import os
import time
import tkinter as tk
from pynput import mouse
from pynput.mouse import Button
from pynput.mouse import Controller


class StartAttacks(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.extra_time = []
        self.controller = controller
        self.mouse = Controller()
        self.break_program = False
        self.canvas = tk.Canvas(self, height=500, width=500, bg="#12454C")
        self.canvas.pack()
        self.label1 = tk.Label(self.canvas, text="Now all you have to do is go to the map, move the application\n"
                                                 "window to the side so it will not cover anything important from\n"
                                                 "the map. Once you press on the START button the auto-attacking will\n"
                                                 "start. If you want to stop it, press the wheel button on the mouse\n"
                                                 "or close the window.",
                               bg="#12454C")
        self.start = tk.Button(self.canvas, text="START", command=self.start_attacking)
        self.back = tk.Button(self.canvas, text="BACK", command=lambda: self.controller.show_frame("MenuPage"))
        self.back.place(x=220, y=400)
        self.label1.place(x=60, y=100)
        self.start.place(x=220, y=250)
        self.delay = 1
        self.jump = []
        self.commanders = []
        self.commanders_time = []
        self.popups = []
        """
        Array containing the wait time after the attacks were launched for every commander.
        """
        self.wait_for_jumps = []
        self.get_data()
        self.final_wait = self.commanders_time[-1][1]
        self.wait = self.commanders_time[0][0]
        self.set_wait_times()

    def get_data(self):
        i = 0
        for filename in os.listdir("Commanders"):
            self.commanders.append([])
            with open(("Commanders/" + filename), 'r') as f:
                my_list = f.readline().split(" ")
                my_list.pop()
                going = int(f.readline().rstrip())
                returning = int(f.readline().rstrip())
                self.commanders_time.append((going, returning))
            for pair in my_list:
                x, y = pair.split(',')
                self.commanders[i].append((x, y))
            f.close()
            i += 1

        j = open("Others/Jump", "r")
        jump_list = j.readline().split(" ")
        jump_list.pop()
        for pair in jump_list:
            x, y = pair.split(',')
            self.jump.append((x, y))
        j.close()
        d = open("Others/Delay", "r")
        self.delay = int(d.readline().rstrip())
        d.close()
        p = open("Others/Popups", "r")
        popups = p.readline().split(" ")
        for pair in popups:
            x, y = pair.split(',')
            self.popups.append((x, y))
        p.close()

    def set_wait_times(self):
        """Check if extra time is needed between attack.
        We will determine this by subtracting the number of seconds the jump takes from the
        seconds it takes for the next attack to be launched.
        """
        for i in range(1, len(self.commanders)):
            difference = 2 * (len(self.commanders[i]) - len(self.jump))
            if difference < 1:
                self.extra_time.append(difference + 1)
            else:
                self.extra_time.append(0)

        for j in range(1, len(self.commanders)):
            self.wait -= 2 * len(self.commanders[j])
            self.wait -= self.extra_time[j - 1]
        self.wait_for_jumps.append(self.wait)
        for i in range(1, len(self.commanders)):
            wait = 2 * len(self.commanders[i])
            wait += (self.commanders_time[i - 1][0] - self.commanders_time[i][0])
            wait -= 2 * len(self.jump)
            self.wait_for_jumps.append(wait)
        """I dont have to wait the full time until the last one reaches home. All I need to do is make sure
        the last one will be home when it is it's turn to attack. If I make sure that this is the case, and
        the commanders are added in the order of their speed, then I can be sure that any commander will be home
        when his turn will come.
        """
        for c in range(len(self.commanders)):
            self.final_wait -= len(self.commanders[c]) * 2
        """Safety measure"""
        self.final_wait += 1

    def on_click(self, x, y, button, pressed):
        if button == mouse.Button.middle and pressed:
            self.break_program = True
            return False

    def start_attacking(self):
        self.break_program = False
        with mouse.Listener(on_click=self.on_click) as listener:
            while not self.break_program:
                self.launch_attack(self.commanders[0])
                for i in range(1, len(self.commanders)):
                    for t in range(self.extra_time[i - 1]):
                        if self.break_program:
                            break
                        time.sleep(1)
                    self.launch_attack(self.commanders[i])

                for j in range(len(self.commanders)):
                    for t in range(self.wait_for_jumps[j]):
                        if self.break_program:
                            break
                        time.sleep(1)
                    self.popup_click()
                    self.do_jump()
                for k in range(self.final_wait):
                    if self.break_program:
                        break
                    time.sleep(1)
            listener.join()

    def launch_attack(self, clicks):
        for click in clicks:
            if self.break_program:
                break
            self.mouse.position = (click[0], click[1])
            time.sleep(self.delay)
            self.mouse.click(Button.left, 1)
            time.sleep(self.delay)

    def do_jump(self):
        for click in self.jump:
            if self.break_program:
                break
            self.mouse.position = (click[0], click[1])
            time.sleep(self.delay)
            self.mouse.click(Button.left, 1)
            time.sleep(self.delay)

    def popup_click(self):
        for click in self.popups:
            if self.break_program:
                break
            self.mouse.position = (click[0], click[1])
            time.sleep(self.delay)
            self.mouse.click(Button.left, 1)
            time.sleep(self.delay)
