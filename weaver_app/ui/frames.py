import tkinter as tk


class HomeFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#282828")
        tk.Label(self, text="Upload File Screen", bg='black', fg='white').pack(expand=True)


class SettingsFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#282828")
        tk.Label(self, text="Ask Question Screen", bg='black', fg='white').pack(expand=True)