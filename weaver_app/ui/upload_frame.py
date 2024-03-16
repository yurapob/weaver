import os
import tkinter as tk
from tkinter import filedialog
from ui.rectangle_button import RectangularButton
from managers.pdf_manager import PDFManager

class UploadFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#282828")

        inner_frame = tk.Frame(self, bg="#282828")
        inner_frame.pack(expand=True)

        listbox_frame = tk.Frame(inner_frame, bg="#282828")
        listbox_frame.pack(pady=(20, 0))

        scrollbar = tk.Scrollbar(listbox_frame, orient="vertical")
        listbox = tk.Listbox(
            listbox_frame,
            width=50,
            height=16,
            yscrollcommand=scrollbar.set,
            bg="black",
            fg="white",
            font=("Courier New", 12)
        )

        scrollbar.config(command=listbox.yview)
        scrollbar.pack(side="right", fill="y")
        listbox.pack(side="left", fill="both", expand=True)

        listbox.insert(tk.END, ">>> your files")

        def on_button_click():
            file_types = [('PDF files', '*.pdf')]
            dialog_title = 'Select a PDF file'
            initial_dir = '/'

            file_path = filedialog.askopenfilename(title=dialog_title, initialdir=initial_dir, filetypes=file_types)
            if file_path:
                file_name = os.path.basename(file_path)
                existing_files = [os.path.basename(existing_path) for existing_path in
                                  PDFManager.get_files()]

                if file_name not in existing_files:
                    PDFManager().add_file(file_path)
                    listbox.insert(tk.END, file_name)
                else:
                    print(">>> File already exists")

        button_text_frame = tk.Frame(inner_frame, bg="#282828")
        button_text_frame.pack(pady=20)

        text_message = (
            "Please upload the PDF file you  \n"
            "intend to explore in the future."
        )
        label = tk.Label(
            button_text_frame,
            text=text_message,
            bg='#282828',
            fg='white',
            font=("Courier New", 16),
            anchor="w"
        )
        label.pack(side="left", fill="x", expand=True)

        button_frame = tk.Frame(button_text_frame, bg="#282828", width=10)
        button_frame.pack(side="left", fill="y")
        button_frame.pack_propagate(False)

        upload_button = RectangularButton(
            button_text_frame,
            text="Upload",
            width=92,
            height=36.5,
            color="white",
            bg="#282828",
            text_color="#282828",
            command=on_button_click
        )
        upload_button.pack(side="left")

        inner_frame.pack(expand=True, anchor='center')
