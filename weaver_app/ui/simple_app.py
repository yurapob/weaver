import tkinter as tk
from ui.frames import HomeFrame, SettingsFrame
from ui.rounded_button import RoundedButton


class SimpleApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Weaver")
        self.geometry("900x600+300+150")
        self.resizable(False, False)

        self.sidebar = tk.Frame(self, width=200, bg="#171717", height=500)
        self.content = tk.Frame(self, bg='red')
        self.frames = {}

        self.init_ui()

    def init_ui(self):
        self.sidebar.pack(side="left", fill="y", expand=False)
        self.sidebar.pack_propagate(False)

        self.content.pack(side="right", fill="both", expand=True)

        for F in (HomeFrame, SettingsFrame):
            frame = F(self.content, self)
            self.frames[F] = frame
            frame.place(x=0, y=0, width=700, height=600)

        self.show_frame(HomeFrame)

        upload_button = RoundedButton(self.sidebar, text="Upload file", width=167, height=44, corner_radius=22,
                                      color="#282828", command=lambda: self.show_frame(HomeFrame))
        upload_button.pack(fill="x", padx=16, pady=(16, 0), ipadx=0, ipady=0)

        ask_button = RoundedButton(self.sidebar, text="Ask question", width=167, height=44, corner_radius=22,
                                   color="#282828", command=lambda: self.show_frame(SettingsFrame))
        ask_button.pack(fill="x", padx=16, pady=(12, 0), ipadx=0, ipady=0)

    def show_frame(self, context):
        frame = self.frames[context]
        frame.tkraise()
