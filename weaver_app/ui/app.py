import tkinter as tk
from ui.upload_frame import UploadFrame
from ui.request_frame import RequestFrame
from ui.rectangle_button import RectangularButton


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Weaver")
        self.geometry("600x350+300+150")
        self.resizable(False, False)

        self.sidebar = tk.Frame(self, width=132, bg="#171717", height=500)
        self.content = tk.Frame(self, bg='red')
        self.frames = {}

        self.init_ui()

    def init_ui(self):
        self.sidebar.pack(side="left", fill="y", expand=False)
        self.sidebar.pack_propagate(False)

        self.content.pack(side="right", fill="both", expand=True)

        for F in (UploadFrame, RequestFrame):
            frame = F(self.content, self)
            self.frames[F] = frame
            frame.place(x=0, y=0, width=468, height=350)

        self.show_frame(UploadFrame)

        upload_button = RectangularButton(
            self.sidebar,
            text="Upload",
            width=100,
            height=44,
            color="#282828",
            bg="#171717",
            text_color="white",
            command=lambda: self.show_frame(UploadFrame)
        )

        upload_button.pack(
            fill="x",
            padx=16,
            pady=(16, 0),
            ipadx=0,
            ipady=0
        )

        ask_button = RectangularButton(
            self.sidebar,
            text="Request",
            width=100,
            height=44,
            color="#282828",
            bg="#171717",
            text_color="white",
            command=lambda: self.show_frame(RequestFrame)
        )

        ask_button.pack(
            fill="x",
            padx=16,
            pady=(12, 0),
            ipadx=0, ipady=0
        )

    def show_frame(self, context):
        frame = self.frames[context]
        frame.tkraise()
