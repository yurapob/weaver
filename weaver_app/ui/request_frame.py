import threading
import tkinter as tk
from ui.rectangle_button import RectangularButton
from managers.chat_manager import DocumentQueryEngine


class RequestFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#282828")

        self.text_widget = tk.Text(
            self,
            wrap=tk.WORD,
            height=250,
            width=428,
            bg="black",
            fg="white",
            font=("Courier New", 12)
        )
        self.text_widget.place(x=20, y=20, width=428, height=250)
        self.text_widget.insert("end", ">>> write your question")
        self.text_widget.configure(state="disabled")

        input_frame = tk.Frame(self, bg="#282828")
        input_frame.pack(side='bottom', fill='x', padx=20, pady=20)

        self.query_entry = tk.Entry(input_frame, font=("Courier New", 14))
        self.query_entry.grid(row=0, column=0, sticky="ew", padx=(0, 10), ipady=6)

        self.submit_button = RectangularButton(
            input_frame,
            text="Submit",
            width=92,
            height=36.5,
            color="#4CAF50",
            bg="#282828",
            text_color="white",
            command=self.submit_query)
        self.submit_button.grid(row=0, column=1)

        input_frame.columnconfigure(0, weight=1)

    def submit_query(self):
        self.update_text_widget(">>> please wait...")
        question = self.query_entry.get()
        thread = threading.Thread(target=self.handle_query, args=(question,))
        thread.start()

    def handle_query(self, question):
        query_engine = DocumentQueryEngine()
        answer = query_engine.ask_question(question)
        self.update_text_widget(answer)

    def update_text_widget(self, answer):
        self.text_widget.configure(state="normal")
        self.text_widget.delete("1.0", "end")
        self.text_widget.insert("end", answer)
        self.text_widget.configure(state="disabled")
