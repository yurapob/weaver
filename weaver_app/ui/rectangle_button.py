import tkinter as tk


class RectangularButton(tk.Canvas):
    def __init__(self, parent, text, width, height, color, bg, text_color, command=None):
        super().__init__(
            parent,
            borderwidth=0,
            highlightthickness=0,
            relief='flat',
            width=width,
            height=height,
            bg=bg
        )

        self.command = command
        self.create_rectangle((0, 0, width, height), fill=color, outline=color)
        self.text_id = self.create_text(
            width / 2,
            height / 2,
            text=text,
            fill=text_color,
            font=("Courier New", 14, "bold")
        )

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