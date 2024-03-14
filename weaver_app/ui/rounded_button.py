import tkinter as tk


class RoundedButton(tk.Canvas):
    def __init__(self, parent, text, width, height, corner_radius, color, command=None):
        tk.Canvas.__init__(self, parent, borderwidth=0, highlightthickness=0, relief='flat', width=width, height=height, bg="#171717")
        self.command = command
        self.text_id = None
        self.create_oval((0, 0, corner_radius * 2, corner_radius * 2), fill=color, outline=color)
        self.create_oval((0, height - corner_radius * 2, corner_radius * 2, height), fill=color, outline=color)
        self.create_oval((width - corner_radius * 2, 0, width, corner_radius * 2), fill=color, outline=color)
        self.create_oval((width - corner_radius * 2, height - corner_radius * 2, width, height), fill=color, outline=color)
        self.create_rectangle((corner_radius, 0, width - corner_radius, height), fill=color, outline=color)
        self.create_rectangle((0, corner_radius, width, height - corner_radius), fill=color, outline=color)
        self.text_id = self.create_text(width / 2, height / 2, text=text, fill="white", font=("Courier New", 14, "bold"))
        self.bind("<ButtonPress-1>", self._on_press)
        self.bind("<ButtonRelease-1>", self._on_release)

    def _on_press(self, event):
        self.configure(relief='sunken')
        if self.text_id:
            self.itemconfig(self.text_id, font=("Courier New", 14, "bold"))

    def _on_release(self, event):
        self.configure(relief='flat')
        if self.command:
            self.command()
        if self.text_id:
            self.itemconfig(self.text_id, font=("Courier New", 14, "bold"))