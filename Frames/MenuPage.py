import tkinter as tk


class MenuPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        canvas = tk.Canvas(self, height=500, width=500, bg="#12454C")
        canvas.pack()

        btn_image = tk.PhotoImage(file="Assets/Delay.png")
        btn_image = btn_image.subsample(2, 2)
        set_delay = tk.Button(canvas, image=btn_image, command=lambda: self.controller.show_frame("ClickDelay"),
                              width=154, height=34, borderwidth=0, activebackground="#12454C", bg="#12454C")
        set_delay.image = btn_image
        set_delay.place(x=50, y=50)

        btn_image = tk.PhotoImage(file="Assets/Popup.png")
        btn_image = btn_image.subsample(2, 2)
        set_popup = tk.Button(canvas, image=btn_image, command=lambda: self.controller.show_frame("Popup"),
                              width=154, height=34, borderwidth=0, activebackground="#12454C", bg="#12454C")
        set_popup.image = btn_image
        set_popup.place(x=50, y=100)

        btn_image = tk.PhotoImage(file="Assets/Jump.png")
        btn_image = btn_image.subsample(2, 2)
        set_jump = tk.Button(canvas, image=btn_image, command=lambda: self.controller.show_frame("JumpClicks"),
                             width=154, height=34, borderwidth=0, activebackground="#12454C", bg="#12454C")
        set_jump.image = btn_image
        set_jump.place(x=50, y=150)

        btn_image = tk.PhotoImage(file="Assets/Add.png")
        btn_image = btn_image.subsample(2, 2)
        add_commander = tk.Button(canvas, image=btn_image, command=lambda: self.controller.show_frame("AddCommander"),
                                  width=154, height=34, borderwidth=0, activebackground="#12454C", bg="#12454C")
        add_commander.image = btn_image
        add_commander.place(x=50, y=200)

        btn_image = tk.PhotoImage(file="Assets/Delete.png")
        btn_image = btn_image.subsample(2, 2)
        delete_commander = tk.Button(canvas, image=btn_image,
                                     command=lambda: self.controller.show_frame("DeleteCommander"),
                                     width=154, height=34, borderwidth=0, activebackground="#12454C", bg="#12454C")
        delete_commander.image = btn_image
        delete_commander.place(x=50, y=250)

        btn_image = tk.PhotoImage(file="Assets/Attack.png")
        btn_image = btn_image.subsample(2, 2)
        attack = tk.Button(canvas, image=btn_image, command=lambda: self.controller.show_frame("StartAttacks"),
                           width=154, height=34, borderwidth=0, activebackground="#12454C", bg="#12454C")
        attack.image = btn_image
        attack.place(x=50, y=300)
