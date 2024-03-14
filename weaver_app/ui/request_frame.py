import tkinter as tk
from ui.rectangle_button import RectangularButton


class RequestFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#282828")
        tk.Label(self, text="Ask Question Screen", bg='black', fg='white').pack(expand=True)