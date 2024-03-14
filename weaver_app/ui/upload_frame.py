import tkinter as tk
from tkinter import filedialog
from ui.rectangle_button import RectangularButton
from managers.pdf_manager import PDFManager


class UploadFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#282828")

        inner_frame = tk.Frame(self, bg="#282828")
        inner_frame.pack(expand=True)

        text_message = (
            "Please upload the PDF \n"
            "file you would like to \n"
            "search through the future"
        )
        label = tk.Label(
            inner_frame,
            text=text_message,
            bg='#282828',
            fg='white',
            font=("Courier New", 22)
        )
        label.pack()

        def on_button_click():
            root = tk.Tk()
            root.withdraw()

            file_types = [('PDF files', '*.pdf')]
            dialog_title = 'Select a PDF file'
            initial_dir = '/'

            file_path = filedialog.askopenfilename(title=dialog_title, initialdir=initial_dir, filetypes=file_types)
            PDFManager.add_file(file_path)

            root.destroy()

        upload_button = RectangularButton(
            inner_frame,
            text="<<< upload >>>",
            width=168,
            height=44,
            color="white",
            bg="#282828",
            text_color="#282828",
            command=on_button_click
        )
        upload_button.pack(pady=20)

        inner_frame.pack(expand=True, anchor='center')